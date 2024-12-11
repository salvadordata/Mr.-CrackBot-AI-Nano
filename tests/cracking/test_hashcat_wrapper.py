import pytest
from cracking.hashcat_wrapper import crack_password

def test_crack_password(monkeypatch):
    def mock_subprocess_run(*args, **kwargs):
        assert "hashcat" in args[0]
    
    monkeypatch.setattr("subprocess.run", mock_subprocess_run)
    crack_password("test.cap", "test_wordlist.txt")
