import pytest
from ai.password_model import generate_password_guesses

def test_generate_password_guesses():
    metadata = {"ssid": "TestNetwork", "bssid": "00:11:22:33:44:55"}
    guesses = generate_password_guesses(metadata)
    assert isinstance(guesses, list)
    assert len(guesses) > 0
