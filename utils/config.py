import os

# General Configuration
PROJECT_NAME = "Mr. CrackBot AI"
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
LOG_FILE = "jetson_crack_ai.log"
LOG_LEVEL = "INFO"

# Ensure required directories exist
os.makedirs(WORDLISTS_DIR, exist_ok=True)
os.makedirs(CAPTURES_DIR, exist_ok=True)
