import pytest
import os
from main import use_combined_wordlist

def test_use_combined_wordlist():
    combined_wordlist_path = "data/wordlists/RockYou2024_combined.txt"
    # Create a mock wordlist file
    os.makedirs(os.path.dirname(combined_wordlist_path), exist_ok=True)
    with open(combined_wordlist_path, "w") as f:
        f.write("password1\npassword2\n")
    
    # Test function
    result = use_combined_wordlist()
    assert result == combined_wordlist_path
    assert os.path.exists(result)

    # Cleanup
    os.remove(combined_wordlist_path)
