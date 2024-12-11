![MrCrackBotAI](docs/screenshots/mrcatbar2.webp)Mr. CrackBot AI Nano

Status: 🚧 In its infancy – Not yet released! Check back soon!

Welcome to Mr. CrackBot AI Nano, a cutting-edge tool designed for automated Wi-Fi penetration testing and password cracking. This README describes the current functionality and tracks the evolution of the project.

🚀 Features 🥷🏻🤖🔥🔥🔥📡👾👾👾👾👾👾👾👾👾

Here’s what Mr. CrackBot AI Nano is designed to accomplish, combining all features into one automated process:
	•	AI-Powered Wordlist Generation: Uses machine learning to generate highly optimized password guesses based on network metadata.
	•	Automated WPA Handshake Capture: Scans networks and captures WPA/WPA2 handshakes with minimal user input. (Currently working on support for WPA3!)
	•	GPU-Accelerated Cracking: Leverages NVIDIA GPUs and tools like hashcat for “lightning-fast”⚡️ password cracking.
	•	Interactive User Interface: Provides real-time updates on cracking progress and network analysis.
![NVIDIAJetsonNano](docs/screenshots/IMG_2246.JPEG)
![HardwareComponents](docs/screenshots/Harware2.JPEG)🛠️ Hardware Components

	1.	NVIDIA Jetson Nano 4GB Kit
	•	Model: 945-13450-0000-000
	•	Price: $135.00
	•	Description: The brain of the operation. This AI development board provides GPU-accelerated processing for CrackBot AI’s tasks. It runs Python scripts efficiently and handles AI workloads for tasks like password cracking and Wi-Fi network analysis.
	2.	WaveShare 7-inch HDMI LCD Touchscreen
	•	Model: 1024x600 USB Capacitive Touch Screen (H)
	•	Price: $42.00
	•	Description: The primary interface for CrackBot AI, allowing interaction via touch. It connects via HDMI for video and USB for touch input.
	3.	18650 Battery Holder (4 Slots)
	•	Model: High-Quality 18650 x4 Battery Storage Clip with 15cm Lead
	•	Price: $2.49
	•	Description: Provides portable power for your setup. Holds four 18650 batteries and connects to the DC power converter to regulate power output.
	4.	18650 3.7V Rechargeable Li-ion Batteries 🔋
	•	Model: 3.7V Li-ion Batteries (x4)
	•	Price: $10.00 (total for 4 batteries)
	•	Description: Rechargeable batteries that supply steady power for extended use.
	5.	4S 18650 Battery Protection Circuit
	•	Model: 4PC 3S 4S 5S BMS 25A Li-ion Battery Protection Board
	•	Price: $11.43
	•	Description: Ensures safe charging/discharging of the batteries and protects against overcharge, over-discharge, and short circuits.
	6.	XL4015 5A Buck DC-DC Power Converter
	•	Model: Step-Down Converter with Voltage Current Display
	•	Price: $8.79
	•	Description: Regulates voltage from the battery pack to provide a stable 5V output for the Jetson Nano and other components.
	7.	HDMI Cable
	•	Model: Ultra-Slim High-Speed HDMI 2.0 Cord (1.5ft)
	•	Price: $8.49
	•	Description: Connects the Jetson Nano to the WaveShare touchscreen for video output.
	8.	TP-Link USB Wi-Fi Adapter
	•	Model: AC600Mbps Archer T2U Plus
	•	Price: $12.99
	•	Description: Provides Wi-Fi connectivity for CrackBot AI, enabling network scanning and interaction.

🛤️ Development Timeline

Phase 1: Conceptualization
	•	Began by creating rough draft firmwares for the ESP32 with a focus on small wordlists.
	•	Pivoted to the NVIDIA Jetson Nano to leverage its GPU for AI-driven cracking.
	•	Integrated wordlists like rockyou2024.txt and SecLists.

Phase 2: Core Functionality Development
	•	AI Wordlist Generation: AI generates custom password guesses based on network metadata.
	•	Handshake Capture: Automated with airodump-ng and aireplay-ng.
	•	Deauthentication Attacks: Forces client reconnections to capture handshakes.

Phase 3: Hardware Integration
	•	Jetson Nano: Optimized for its hardware constraints.
	•	Wi-Fi Adapter: Verified monitor mode compatibility.
	•	GPU Utilization: Added hashcat for GPU-accelerated cracking.

Phase 4: Interactive User Interface
	•	Added a user-friendly UI for monitoring networks and cracking progress.
	•	Enabled real-time updates on handshake status.

Phase 5: Setup & Configuration Initialization
	•	Modified setup.py to:
	•	Auto-install dependencies and requirements from requirements.txt.
	•	Download the two rockyou2024.txt files from my Mega cloud repository.
	•	Automatically extract and combine the files into a plaintext wordlist.

📜 Handling the rockyou2024.txt File

The setup process has been streamlined to automatically download, extract, and combine the massive rockyou2024.txt wordlists. The combined file is ready to use out of the box for password cracking.

🛠️ Installation
	1.	Clone the Repository:

git clone https://github.com/<your-username>/Mr.-CrackBot-AI-Nano.git
cd Mr.-CrackBot-AI-Nano


	2.	Run the Program:
Simply execute the main script:

python main.py

	•	What Happens Automatically:
	•	setup.py handles all setup tasks:
	•	Auto-installs dependencies.
	•	Downloads and combines rockyou2024.txt from the Mega cloud repository.
	•	Creates required directories.
	•	Prepares the system for immediate use.

⚠️ Disclaimer:
This project is for educational purposes only. Use responsibly and only on networks you own or have permission to test.

🤝 Contributing:
	•	Open issues for bugs or feature requests.
	•	Submit pull requests for new features.
