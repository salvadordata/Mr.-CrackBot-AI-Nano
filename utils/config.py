import os
import shutil
import yaml  # For loading YAML files


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
    NETWORK_INTERFACE = "wlan0mon"
    CAPTURE_TIMEOUT = 60

    # Cracking Configuration
    HASHCAT_MODE = 2500
    HASHCAT_OPTIONS = "--force --opencl-device-types=1,2"

    # Logging Configuration
    LOG_FILE = "mr_crackbot_ai.log"
    LOG_LEVEL = "INFO"

    # Temporary Directory
    TEMP_DIRECTORY = "temp"
    TEMP_DIRECTORY_ENABLED = True

    # Additional Configurations
    ENABLE_GPU = True
    MAX_THREADS = 8

    # Tool Paths
    AIRODUMP_PATH = "/usr/bin/airodump-ng"
    AIREPLAY_PATH = "/usr/bin/aireplay-ng"
    HASHCAT_PATH = "/usr/bin/hashcat"

    # Wordlist Management
    COMBINED_WORDLIST = "data/wordlists/combined_rockyou2024.txt"
    WORDLIST_CHUNK_SIZE = 100000

    # Security Features
    ENABLE_SANDBOX = False
    ENFORCE_SAFE_MODE = True

    # User Interface
    UI_THEME = "dark"
    ENABLE_ANIMATIONS = True

    # Notifications
    SEND_EMAIL_ALERTS = False
    EMAIL_RECIPIENT = "admin@example.com"

    # Debugging Options
    ENABLE_DEBUG_MODE = False
    VERBOSE_OUTPUT = True

    # GPU Configuration for Jetson Nano
    CUDA_PATH = "/usr/local/cuda"
    GPU_DEVICE_ID = 0
    GPU_MAX_MEMORY = 90
    GPU_FORCE_USAGE = True

    @classmethod
    def load_from_file(cls, file_path="config.yaml"):
        """Load configuration settings from a YAML file and override default values."""
        try:
            with open(file_path, "r") as file:
                config_data = yaml.safe_load(file)

            for key, value in config_data.items():
                if hasattr(cls, key.upper()):
                    setattr(cls, key.upper(), value)
                else:
                    print(f"[WARNING] Unknown config key: {key}")

            print("[*] Configuration successfully loaded from file.")
        except FileNotFoundError:
            print(f"[!] Configuration file not found: {file_path}")
        except yaml.YAMLError as e:
            print(f"[!] Error parsing YAML configuration file: {e}")

    @classmethod
    def get_combined_wordlist_path(cls):
        """Get the combined wordlist path, fallback to DEFAULT_WORDLIST."""
        return getattr(cls, "COMBINED_WORDLIST", cls.DEFAULT_WORDLIST)


# Automatically load the configuration on import
Config.load_from_file()


# Ensure required directories exist
def ensure_directories():
    """Ensure all required directories for the project exist."""
    required_dirs = [
        Config.WORDLISTS_DIR,
        Config.CAPTURES_DIR,
        Config.TEMP_DIRECTORY,
    ]
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


# Check if required Python libraries are installed
def check_python_dependencies():
    """Ensure required Python libraries are installed."""
    try:
        import transformers  # noqa: F401
    except ImportError:
        print("[*] Transformers library not found. Installing...")
        os.system("pip install transformers")
        print("[*] Transformers library installed successfully.")


def validate_environment():
    """Validate the environment setup by ensuring directories, tools, and dependencies are in place."""
    try:
        ensure_directories()
        check_prerequisites()
        check_python_dependencies()
        print("[*] Environment validation complete.")
    except Exception as e:
        print(f"[!] Environment validation failed: {e}")
        exit(1)

