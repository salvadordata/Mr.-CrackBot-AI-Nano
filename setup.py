import os
import subprocess

def create_directories():
    """
    Ensure all required directories are created during setup.
    """
    directories = [
        "data/wordlists",
        "data/captures",
        "logs",
        "custom_wordlists",
        "screenshots",
        "docs/screenshots",
        "build",
        "dist",
        "env",
        "venv",
        "node_modules",
        "jetson_logs",
    ]
    for directory in directories:
        if not os.path.exists(directory):
            print(f"[*] Creating directory: {directory}")
            os.makedirs(directory)
    print("[*] All required directories have been created.")

def download_and_extract_wordlists():
    """
    Download, extract, and combine RockYou2024 wordlists from external sources.
    """
    # URLs of the RockYou2024.7z files
    mega_links = [
        "https://mega.nz/file/vUIyFJQT#phrB_D2B9GMUmBkqcj2Be4y8rVAFdSMRhjj9GmS9r_w",
        "https://mega.nz/file/6QpViJzA#FFoIHZ68MRkhDB1j2qaqgLyaf3v1MPrArQoU3OnyJbs"
    ]
    output_dir = "data/wordlists"
    combined_wordlist = os.path.join(output_dir, "RockYou2024_combined.txt")

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Step 1: Download the .7z files
    for link in mega_links:
        print(f"Downloading {link}...")
        subprocess.run(["megadl", link, "--path", output_dir], check=True)

    # Step 2: Extract the .7z files
    extracted_files = []
    for file in os.listdir(output_dir):
        if file.endswith(".7z"):
            filepath = os.path.join(output_dir, file)
            print(f"Extracting {filepath}...")
            subprocess.run(["7z", "x", filepath, f"-o{output_dir}"], check=True)
            # Collect extracted .txt files
            extracted_files.extend(
                os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith(".txt")
            )
            print(f"Extracted {file}.")

    # Step 3: Combine extracted .txt files
    print(f"Combining extracted wordlists into {combined_wordlist}...")
    with open(combined_wordlist, "w") as outfile:
        for txt_file in extracted_files:
            with open(txt_file, "r", encoding="utf-8", errors="ignore") as infile:
                outfile.write(infile.read())
    print(f"Combined wordlist saved as {combined_wordlist}.")

def ensure_dependencies():
    """
    Install necessary dependencies like MegaCMD.
    """
    print("[*] Installing MegaCMD for downloading...")
    subprocess.run(["sudo", "apt-get", "install", "-y", "megatools"], check=True)

# Setup script
if __name__ == "__main__":
    print("[*] Creating required directories...")
    create_directories()

    print("[*] Ensuring dependencies...")
    ensure_dependencies()

    print("[*] Downloading, extracting, and combining RockYou2024 wordlists...")
    download_and_extract_wordlists()