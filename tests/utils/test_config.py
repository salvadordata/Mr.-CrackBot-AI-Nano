import pytest
from utils.config import ensure_directories, check_prerequisites

def test_ensure_directories():
    ensure_directories()
    directories = ["data/wordlists", "data/captures"]
    for directory in directories:
        assert os.path.exists(directory)
        os.rmdir(directory)
