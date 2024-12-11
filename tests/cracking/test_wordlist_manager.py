import pytest
from cracking.wordlist_manager import WordlistManager

def test_generate_wordlist():
    manager = WordlistManager()
    wordlist = manager.generate_wordlist({"ssid": "TestNetwork"})
    assert isinstance(wordlist, list)
    assert len(wordlist) > 0
