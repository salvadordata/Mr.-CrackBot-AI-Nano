import pytest
from network.handshake import capture_handshake

def test_capture_handshake(monkeypatch):
    def mock_subprocess_run(*args, **kwargs):
        assert "airodump-ng" in args[0]
    
    monkeypatch.setattr("subprocess.run", mock_subprocess_run)
    result = capture_handshake("mock_bssid", "6")
    assert result == "data/captures/handshake-01.cap"
