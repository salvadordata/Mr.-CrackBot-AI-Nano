import os
import shutil

# General Configuration
PROJECT_NAME = "Mr. Crackbot AI"
VERSION = "1.0"

# Data Directories
DATA_DIR = "data"
WORDLISTS_DIR = os.path.join(DATA_DIR, "wordlists")
CAPTURES_DIR = os.path.join(DATA_DIR, "captures")

# Default Wordlist Files
DEFAULT_WORDLIST = os.path.join(WORDLISTS_DIR, "rockyou2024.txt")
GENERATED_WORDLIST = os.path.join(WORDLISTS_DIR, "generated.txt")

# Network Configuration
NETWORK_INTERFACE = "wlan0mon"  # Default wireless interface for scanning/attacking
CAPTURE_TIMEOUT = 60  # Timeout for handshake capture in seconds

# Cracking Configuration
HASHCAT_MODE = 2500  # WPA/WPA2 cracking mode
HASHCAT_OPTIONS = "--force"  # Default options for Hashcat

# Logging Configuration
LOG_FILE = "mr._crackbot_ai.log"
LOG_LEVEL = "INFO"

# Ensure required directories exist
def ensure_directories():
    """Ensure all required directories for the project exist."""
    required_dirs = [WORDLISTS_DIR, CAPTURES_DIR]
    for directory in required_dirs:
        os.makedirs(directory, exist_ok=True)
    print("[*] All necessary directories are set up.")

# Check if required tools are installed
def check_prerequisites():
    """Ensure all required tools are installed on the system."""
    required_tools = ["airodump-ng", "aireplay-ng", "hashcat"]
    missing_tools = [tool for tool in required_tools if shutil.which(tool) is None]
    if missing_tools:
        raise RuntimeError(f"Missing required tools: {', '.join(missing_tools)}")
    print("[*] All required tools are installed.")
