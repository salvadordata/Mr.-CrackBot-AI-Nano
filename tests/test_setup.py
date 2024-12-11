import pytest
import os
import subprocess
from setup import create_directories, download_and_extract_wordlists

def test_create_directories():
    directories = [
        "data/wordlists", "data/captures", "logs",
        "custom_wordlists", "screenshots", "docs/screenshots"
    ]
    create_directories()
    for directory in directories:
        assert os.path.exists(directory)
        os.rmdir(directory)

def test_download_and_extract_wordlists(monkeypatch):
    # Mock subprocess call
    def mock_subprocess_run(*args, **kwargs):
        assert "megadl" in args[0] or "7z" in args[0]
    
    monkeypatch.setattr(subprocess, "run", mock_subprocess_run)
    download_and_extract_wordlists()
