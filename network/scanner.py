import subprocess

def scan_networks(interface="wlan0mon"):
    output_file = "data/captures/scan_results.csv"
    command = f"airodump-ng --write {output_file} --output-format csv {interface}"
    subprocess.run(command, shell=True)

    return parse_scan_results(output_file)

def parse_scan_results(file_path):
    # Parses airodump-ng's CSV output
    networks = []
    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("Station"):
                break  # Skip station info
            if "BSSID" not in line:  # Ignore header
                parts = line.split(",")
                if len(parts) > 13:  # Ensure valid network
                    networks.append({
                        "bssid": parts[0].strip(),
                        "ssid": parts[13].strip(),
                        "channel": parts[3].strip()
                    })
    return networks
