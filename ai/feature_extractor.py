def extract_features(ssid, bssid):
    return {
        "ssid": ssid,
        "bssid_prefix": bssid[:8],  # First 8 characters of BSSID
        "patterns": [ssid.upper(), ssid.lower(), bssid.replace(":", "")]
    }
