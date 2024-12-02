1   import subprocess

3   def crack_password(handshake_file, wordlist_file, progress_callback=None):
4       """
5       Crack a WPA handshake using hashcat with optional progress updates.
6       :param handshake_file: Path to the handshake file (in .hccapx format).
7       :param wordlist_file: Path to the wordlist file.
8       :param progress_callback: A function to call with progress updates.
9       """
10      try:
11          print(f"[*] Starting password cracking for: {handshake_file}")
12          process = subprocess.Popen(
13              [
14                  "hashcat",
15                  "-m", "2500",  # WPA2 hash mode
16                  handshake_file,
17                  wordlist_file,
18                  "--status",
19                  "--status-timer=10",
20                  "--quiet"
21              ],
22              stdout=subprocess.PIPE,
23              stderr=subprocess.PIPE,
24              universal_newlines=True
25          )

27          cracked_password = None
28          for line in process.stdout:
29              print(line.strip())
30              # Detect progress updates
31              if progress_callback and "Progress" in line:
32                  progress_value = parse_progress(line)
33                  progress_callback(progress_value)
34              # Detect cracked password
35              if "Cracked" in line or "Found" in line:
36                  cracked_password = parse_cracked_password(line)
37                  break

39          process.wait()
40          if cracked_password:
41              print(f"[+] Password successfully cracked: {cracked_password}")
42              save_cracked_password(handshake_file, cracked_password)
43          else:
44              print("[!] Password cracking failed or no result.")

46      except Exception as e:
47          print(f"[!] Error during cracking: {e}")

49  def parse_progress(line):
50      """
51      Parse progress percentage from hashcat output.
52      Example: "Progress: 50%"
53      """
54      try:
55          return int(line.split("Progress:")[1].split("%")[0].strip())
56      except (IndexError, ValueError):
57          return 0

59  def parse_cracked_password(line):
60      """
61      Parse the cracked password from hashcat output.
62      Example: "Cracked: mypassword123"
63      """
64      try:
65          return line.split(":")[1].strip()
66      except IndexError:
67          return None

69  def save_cracked_password(handshake_file, password):
70      """
71      Save the cracked password to a results file.
72      :param handshake_file: The handshake file path.
73      :param password: The cracked password.
74      """
75      results_file = "data/results.txt"
76      with open(results_file, "a") as file:
77          file.write(f"{handshake_file}: {password}\n")
78      print(f"[+] Cracked password saved to {results_file}")