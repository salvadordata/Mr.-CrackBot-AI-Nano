import subprocess

def crack_password(handshake_file, wordlist_file, progress_callback=None):
    """
    Crack a WPA handshake using hashcat with optional progress updates.
    :param handshake_file: Path to the handshake file (in .hccapx format).
    :param wordlist_file: Path to the wordlist file.
    :param progress_callback: A function to call with progress updates.
    """
    try:
        print(f"[*] Starting password cracking for: {handshake_file}")
        process = subprocess.Popen(
            [
                "hashcat",
                "-m", "2500",  # WPA2 hash mode
                handshake_file,
                wordlist_file,
                "--status",
                "--status-timer=10",
                "--quiet"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        cracked_password = None
        for line in process.stdout:
            print(line.strip())
            # Detect progress updates
            if progress_callback and "Progress" in line:
                progress_value = parse_progress(line)
                progress_callback(progress_value)
            # Detect cracked password
            if "Cracked" in line or "Found" in line:
                cracked_password = parse_cracked_password(line)
                break

        process.wait()
        if cracked_password:
            print(f"[+] Password successfully cracked: {cracked_password}")
            save_cracked_password(handshake_file, cracked_password)
        else:
            print("[!] Password cracking failed or no result.")

    except Exception as e:
        print(f"[!] Error during cracking: {e}")

def parse_progress(line):
    """
    Parse progress percentage from hashcat output.
    Example: "Progress: 50%"
    """
    try:
        return int(line.split("Progress:")[1].split("%")[0].strip())
    except (IndexError, ValueError):
        return 0

def parse_cracked_password(line):
    """
    Parse the cracked password from hashcat output.
    Example: "Cracked: mypassword123"
    """
    try:
        return line.split(":")[1].strip()
    except IndexError:
        return None

def save_cracked_password(handshake_file, password):
    """
    Save the cracked password to a results file.
    :param handshake_file: The handshake file path.
    :param password: The cracked password.
    """
    results_file = "data/results.txt"
    with open(results_file, "a") as file:
        file.write(f"{handshake_file}: {password}\n")
    print(f"[+] Cracked password saved to {results_file}")
