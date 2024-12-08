import os
import requests

def download_rockyou2024():
    # URL of the RockYou2024.txt file
    url = "https://github.com/trstout/RockYou2024/raw/main/RockYou2024.txt"
    # Path where the file should be saved
    output_path = "data/rockyou2024.txt"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Download the file
    print(f"Downloading {url}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Downloaded RockYou2024.txt to {output_path}")
    else:
        print(f"Failed to download the file. HTTP Status Code: {response.status_code}")

if __name__ == "__main__":
    download_rockyou2024()
