from ai.password_model import PasswordGenerator

class WordlistManager:
    def __init__(self):
        self.generator = PasswordGenerator()

    def generate_wordlist(self, features):
        prompt = f"SSID: {features['ssid']}, BSSID: {features['bssid_prefix']}"
        words = self.generator.generate(prompt)
        wordlist_path = "data/wordlists/generated.txt"
        with open(wordlist_path, "w") as file:
            file.write("\n".join(words))
        return wordlist_path
