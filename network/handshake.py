import subprocess
import re  # Added for detecting WPA handshake in logs


def capture_handshake(bssid, channel, interface="wlan0mon"):
    """
    Capture a WPA handshake for the given network and auto-process it.
    :param bssid: The BSSID of the target network.
    :param channel: The channel of the target network.
    :param interface: The wireless interface to use (default: wlan0mon).
    """
    output_file = f"data/captures/handshake_{bssid}"
    command = [
        "airodump-ng",
        "--bssid",
        bssid,
        "--channel",
        str(channel),
        "--write",
        output_file,
        interface,
    ]

    try:
        print(f"[*] Switching to channel {channel}...")
        subprocess.run(["iwconfig", interface, "channel", str(channel)], check=True)

        print(f"[*] Capturing handshake for BSSID {bssid} on channel {channel}...")
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

        for line in process.stdout:
            print(line.strip())  # Log airodump-ng output
            # Detect handshake capture in the output
            if "WPA handshake:" in line:
                print("[*] Handshake successfully captured!")
                handshake_file = f"{output_file}-01.cap"
                process.terminate()  # Stop capturing once handshake is detected
                auto_process_handshake(handshake_file)
                break

    except subprocess.CalledProcessError as e:
        print(f"[!] Error during handshake capture: {e}")


def auto_process_handshake(handshake_file):
    """
    Automatically process a captured handshake for cracking.
    :param handshake_file: Path to the captured handshake file.
    """
    print(f"[*] Processing handshake: {handshake_file}")
    hccapx_file = handshake_file.replace(".cap", ".hccapx")
    try:
        subprocess.run(["hcxpcaptool", "-o", hccapx_file, handshake_file], check=True)
        print(f"[*] Handshake converted for hashcat: {hccapx_file}")
        # Here, you can call the cracking function
        # Example:
        # crack_password(hccapx_file, "data/wordlists/generated.txt")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error during handshake processing: {e}")