import os
import shutil

# General Configuration
PROJECT_NAME = "Jetson Crack AI"
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

# Utility Functions
def get_data_directory():
    """Return the base data directory."""
    return DATA_DIR

def get_wordlists_directory():
    """Return the wordlists directory."""
    return WORDLISTS_DIR

def get_captures_directory():
    """Return the captures directory."""
    return CAPTURES_DIR

def log_message(message):
    """Log a message (placeholder for future logging functionality)."""
    print(f"[LOG] {message}")

def print_configuration():
    """Print the current configuration settings."""
    print("===== Jetson Crack AI Configuration =====")
    print(f"Project Name: {PROJECT_NAME}")
    print(f"Version: {VERSION}")
    print(f"Data Directory: {DATA_DIR}")
    print(f"Wordlists Directory: {WORDLISTS_DIR}")
    print(f"Captures Directory: {CAPTURES_DIR}")
    print(f"Default Wordlist: {DEFAULT_WORDLIST}")
    print(f"Generated Wordlist: {GENERATED_WORDLIST}")
    print(f"Network Interface: {NETWORK_INTERFACE}")
    print(f"Capture Timeout: {CAPTURE_TIMEOUT} seconds")
    print(f"Hashcat Mode: {HASHCAT_MODE}")
    print(f"Hashcat Options: {HASHCAT_OPTIONS}")
    print(f"Log File: {LOG_FILE}")
    print(f"Log Level: {LOG_LEVEL}")
    print("=========================================")

def validate_environment():
    """
    Validate the environment setup by ensuring directories, tools, and dependencies are in place.
    Combines ensure_directories() and check_prerequisites() into a single call.
    """
    try:
        ensure_directories()
        check_prerequisites()
        print("[*] Environment validation complete.")
    except Exception as e:
        print(f"[!] Environment validation failed: {e}")
        exit(1)
