![MrCrackBotAI](docs/screenshots/mrcatbar2.webp)

# Mr. CrackBot AI

> **Status**: 🚧 In its infancy – Not yet released!

Welcome to **Mr. CrackBot AI**, a cutting-edge tool designed for automated Wi-Fi penetration testing and password cracking. This README not only describes the current functionality but also tracks the evolution of the project.

---

## 🚀 Features
Here’s what Mr. CrackBot AI aims to accomplish:
- **AI-Powered Wordlist Generation**: Uses machine learning to generate highly optimized password guesses based on network metadata.
- **Automated WPA Handshake Capture**: Scans networks and captures WPA/WPA2 handshakes with minimal user input.
- **GPU-Accelerated Cracking**: Leverages NVIDIA GPUs and tools like `hashcat` for lightning-fast password cracking.
- **Interactive User Interface**: Provides real-time updates on cracking progress and network analysis.

---

## 🛠️ Hardware Requirements
To run Mr. CrackBot AI, you’ll need:
- **NVIDIA Jetson Nano (4GB)**:
  - A small yet powerful AI development board.
- **Wi-Fi Adapter**:
  - Capable of monitor mode (e.g., ALFA AWUS036ACH).
- **NVIDIA GPU** (optional):
  - Enhances cracking speed if using external hardware. Its an idea I'm toying with
- **SD Card**:
  - Minimum 32GB with Mr. CrackBot AI ISO installed.
    
---

## 🛤️ Development Timeline

### **Phase 1: Conceptualization**
- **Initial Idea**: The project began with discussions about creating a firmware for the NVIDIA Jetson Nano to automate Wi-Fi password cracking.
- **Key Focus**:
  - Leveraging the GPU for AI-driven password cracking.
  - Using wordlists like `rockyou2024.txt` and `SecLists` for cracking WPA/WPA2 passwords.

---

### **Phase 2: Core Functionality Development**
- **AI Wordlist Generation**:
  - Integrated an AI model to generate customized password guesses based on SSID and BSSID metadata.
- **Handshake Capture**:
  - Automated handshake capturing using tools like `airodump-ng` and `aireplay-ng`.
- **Deauthentication Attacks**:
  - Added functionality to force client reconnections for handshake collection.

---

### **Phase 3: Hardware Integration**
- **Jetson Nano**:
  - Optimized the project for the Jetson Nano, ensuring compatibility with its hardware constraints.
- **Wi-Fi Adapter Setup**:
  - Tested and verified monitor mode compatibility with various adapters.
- **GPU Utilization**:
  - Integrated `hashcat` for GPU-accelerated cracking.

---

### **Phase 4: Interactive User Interface**
- **UI Design**:
  - Added a user-friendly interface for monitoring networks, handshake capture, and cracking progress.
- **Real-Time Updates**:
  - Enabled live tracking of handshake capture status and cracking progress in the UI.

---

### **Phase 5: Configuration Initialization**
- **Error Handling**:
  - Ensured the project validates required tools (e.g., `airodump-ng`, `aireplay-ng`, `hashcat`) before starting.
- **Directory Setup**:
  - Automated the creation of necessary directories (e.g., `data/wordlists`, `data/captures`) during initialization.

---

## 🧠 How It Works
1. **Scanning Networks**:
   - The system uses `airodump-ng` to discover nearby Wi-Fi networks and identifies potential targets.

2. **Capturing Handshakes**:
   - Handshakes are captured using deauthentication attacks (`aireplay-ng`) and stored for analysis.

3. **AI-Powered Wordlists**:
   - Based on network metadata (SSID, BSSID), the AI generates custom wordlists optimized for cracking.

4. **GPU Cracking**:
   - The generated wordlist is run through `hashcat` for GPU-accelerated password cracking.

---

## 🛠️ Installation
To set up Mr. CrackBot AI:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mr-crackbot-ai.git
   cd mr-crackbot-ai

	2.	Install dependencies:

pip install -r requirements.txt


	3.	Flash the ISO to your SD card and boot your Jetson Nano.

⚠️ Disclaimer

This project is for educational purposes only. Use responsibly and only on networks you own or have permission to test.

🤝 Contributing

Contributions are welcome! Here’s how you can help:
	•	Open issues for bugs or feature requests.
	•	Submit pull requests for new features.

📜 License

This project is licensed under the MIT License.

📊 Project Status

---

