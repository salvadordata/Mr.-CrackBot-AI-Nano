import subprocess

def crack_password(handshake_file, wordlist_file):
    command = f"hashcat -m 2500 {handshake_file} {wordlist_file} --force"
    subprocess.run(command, shell=True)
