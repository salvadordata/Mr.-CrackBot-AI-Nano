import os
import shutil

class Config:
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
    LOG_FILE = "mr_crackbot_ai.log"
    LOG_LEVEL = "INFO"

# Ensure required directories exist
def ensure_directories():
    """Ensure all required directories for the project exist."""
    required_dirs = [Config.WORDLISTS_DIR, Config.CAPTURES_DIR]
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
    return Config.DATA_DIR

def get_wordlists_directory():
    """Return the wordlists directory."""
    return Config.WORDLISTS_DIR

def get_captures_directory():
    """Return the captures directory."""
    return Config.CAPTURES_DIR

def log_message(message):
    """Log a message (placeholder for future logging functionality)."""
    print(f"[LOG] {message}")

def print_configuration():
    """Print the current configuration settings."""
    print("===== Mr. CrackBot AI Configuration =====")
    print(f"Project Name: {Config.PROJECT_NAME}")
    print(f"Version: {Config.VERSION}")
    print(f"Data Directory: {Config.DATA_DIR}")
    print(f"Wordlists Directory: {Config.WORDLISTS_DIR}")
    print(f"Captures Directory: {Config.CAPTURES_DIR}")
    print(f"Default Wordlist: {Config.DEFAULT_WORDLIST}")
    print(f"Generated Wordlist: {Config.GENERATED_WORDLIST}")
    print(f"Network Interface: {Config.NETWORK_INTERFACE}")
    print(f"Capture Timeout: {Config.CAPTURE_TIMEOUT} seconds")
    print(f"Hashcat Mode: {Config.HASHCAT_MODE}")
    print(f"Hashcat Options: {Config.HASHCAT_OPTIONS}")
    print(f"Log File: {Config.LOG_FILE}")
    print(f"Log Level: {Config.LOG_LEVEL}")
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
