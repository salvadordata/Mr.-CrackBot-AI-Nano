import subprocess

def capture_handshake(bssid, channel, interface="wlan0mon"):
    output_file = "data/captures/handshake"
    command = f"airodump-ng --bssid {bssid} --channel {channel} --write {output_file} {interface}"
    subprocess.run(command, shell=True)
    return f"{output_file}-01.cap"
