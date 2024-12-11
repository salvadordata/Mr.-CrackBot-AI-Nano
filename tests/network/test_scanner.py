import pytest
from network.scanner import scan_networks

def test_scan_networks():
    networks = scan_networks()
    assert isinstance(networks, list)
    for network in networks:
        assert "ssid" in network
        assert "bssid" in network
        assert "channel" in network
