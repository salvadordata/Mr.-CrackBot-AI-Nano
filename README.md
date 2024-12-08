![MrCrackBotAI](docs/screenshots/mrcatbar2.webp)

Mr. CrackBot AI

	Status: 🚧 In its infancy – Not yet released!

Welcome to Mr. CrackBot AI, a cutting-edge tool designed for automated Wi-Fi penetration testing and password cracking. This README describes the current functionality and also tracks the evolution of the project.

🚀 Features🥷🏻🤖🔥🔥🔥📡👾👾👾👾👾👾👾👾👾

Here’s what Mr. CrackBot AI aims to accomplish, combining all of these features into one automatic process:
	•	AI-Powered Wordlist Generation: Uses machine learning to generate highly optimized password guesses based on network metadata.
	•	Automated WPA Handshake Capture: Scans networks and captures WPA/WPA2 handshakes with minimal user input. Working on attempting WPA3…
	•	GPU-Accelerated Cracking: Leverages NVIDIA GPUs and tools like hashcat for “lightning-fast”⚡️💤💤💤💾📡👾password cracking.
	•	Interactive User Interface: Provides real-time updates on cracking progress and network analysis.

![NVIDIAJetsonNano](docs/screenshots/IMG_2246.jpeg)


## Hardware Components 🛠️

---

![HardwareComponents](docs/screenshots/Harware2.JPEG)


	1.	NVIDIA Jetson Nano 4GB Kit
	•	Model: 945-13450-0000-000
	•	Price: $135.00
	•	Description: The brain of the operation, this AI development board provides GPU-accelerated processing for CrackBot AI’s tasks. It runs Python scripts efficiently and handles AI workloads for tasks like password cracking and Wi-Fi network analysis.
	2.	WaveShare 7-inch HDMI LCD Touchscreen
	•	Model: 1024x600 USB Capacitive Touch Screen (H)
	•	Price: $42.00
	•	Description: This display is the primary interface for CrackBot AI, allowing you to interact with the software via touch. It connects via HDMI for video and USB for touch input.
	3.	18650 Battery Holder (4 Slots)
	•	Model: High-Quality 18650 x4 Battery Storage Clip with 15cm Lead
	•	Price: $2.49
	•	Description: Provides portable power for your setup. Holds four 18650 batteries and connects to the DC power converter to regulate power output.
	4.	18650 3.7V Rechargeable Li-ion Batteries 🔋
	•	Model: 3.7V Li-ion Batteries (x4)
	•	Price: $10.00 (estimated total for 4 batteries)
	•	Description: The primary power source for CrackBot AI. These rechargeable batteries provide a steady power supply for extended use.
	5.	4S 18650 Battery Protection Circuit
	•	Model: 4PC 3S 4S 5S BMS 25A Li-ion Battery Protection Board
	•	Price: $11.43
	•	Description: Ensures safe charging and discharging of the 18650 batteries. Protects against overcharge, over-discharge, and short circuits.
	6.	XL4015 5A Buck DC-DC Power Converter
	•	Model: Step Down Converter with Voltage Current Display
	•	Price: $8.79
	•	Description: Regulates voltage from the battery pack to supply a stable 5V output for the Jetson Nano and other components.
	7.	HDMI Cable
	•	Model: Ultra-Slim High-Speed HDMI 2.0 Cord (1.5ft)
	•	Price: $8.49
	•	Description: Connects the Jetson Nano to the WaveShare touchscreen for video output.
	8.	16.8V 2A AC/DC Charger
	•	Model: Adapter for 4S 18650 Li-ion Battery Pack
	•	Price: $7.55
	•	Description: Charges the 18650 battery pack to ensure uninterrupted operation.
	9.	TP-Link USB Wi-Fi Adapter
	•	Model: AC600Mbps Archer T2U Plus
	•	Price: $12.99
	•	Description: Provides Wi-Fi connectivity for CrackBot AI, enabling network scanning and interaction.

Total Estimated Cost: ~$238.74

🛤️ Development Timeline

Phase 1: Conceptualization
	•	Initial Idea: I began by creating several rough draft firmwares for an ESP32 device called the Cheap Yellow Display. The goal was running shorter wordlists in auto mode, but I pivoted to researching the smallest, most powerful SBCs capable of password cracking—and found the NVIDIA Jetson Nano!
	•	Key Focus:
	•	Leveraging the GPU for AI-driven password cracking.
	•	Using wordlists like rockyou2024.txt and SecLists for cracking WPA/WPA2 passwords.

Phase 2: Core Functionality Development
	•	AI Wordlist Generation:
	•	Integrated an AI model to generate customized password guesses based on SSID and BSSID metadata.
	•	Handshake Capture:
	•	Automated handshake capturing using tools like airodump-ng and aireplay-ng.
	•	Deauthentication Attacks:
	•	Added functionality to force client reconnections for handshake collection.

Phase 3: Hardware Integration
	•	Jetson Nano:
	•	Optimized the project for the Jetson Nano, ensuring compatibility with its hardware constraints.
	•	Wi-Fi Adapter Setup:
	•	Tested and verified monitor mode compatibility with various adapters.
	•	GPU Utilization:
	•	Integrated hashcat for GPU-accelerated cracking.

Phase 4: Interactive User Interface
	•	UI Design:
	•	Added a user-friendly interface for monitoring networks, handshake capture, and cracking progress.
	•	Real-Time Updates:
	•	Enabled live tracking of handshake capture status and cracking progress in the UI.

Phase 5: Configuration Initialization
	•	Error Handling:
	•	Ensured the project validates required tools (e.g., airodump-ng, aireplay-ng, hashcat) before starting.
	•	Directory Setup:
	•	Automated the creation of necessary directories (e.g., data/wordlists, data/captures) during initialization.

✨ Update: Docker Image and AI Integration

The latest development includes:
	•	Dockerized Environment: A fully-functional Docker image for streamlined deployment and testing.
	•	AI-Driven Password Cracking: Hugging Face GPT-2 integration for generating adaptive, metadata-based wordlists.

The system can now process network metadata such as SSID, location, and known parameters to create highly targeted password guesses. These AI-driven wordlists are further optimized using pattern-based techniques and logged for transparency and debugging.

🧠 How It Works
	1.	Scanning Networks:
	•	The system uses airodump-ng to discover nearby Wi-Fi networks and identifies potential targets.
	2.	Capturing Handshakes:
	•	Handshakes are captured using deauthentication attacks (aireplay-ng) and stored for analysis.
	3.	AI-Powered Wordlists:
	•	Based on network metadata (SSID, BSSID), the AI generates custom wordlists optimized for cracking.
	4.	GPU Cracking:
	•	The generated wordlist is run through hashcat for GPU-accelerated password cracking.

📜 Handling the rockyou2024.txt File

Given the large size of rockyou2024.txt, the setup process now includes splitting the file into manageable chunks for better performance:
	1.	Automatic Splitting During Setup:
	•	The setup.py script handles splitting automatically:

import os
import subprocess

rockyou_path = "data/rockyou2024.txt"
split_output_dir = "data/split_rockyou"
os.makedirs(split_output_dir, exist_ok=True)
subprocess.run(["split", "-l", "100000", rockyou_path, f"{split_output_dir}/rockyou_part_"])


	2.	Standalone Splitting Script:
	•	You can run the split_wordlist.sh script manually:

#!/bin/bash
rockyou_path="data/rockyou2024.txt"
split_output_dir="data/split_rockyou"
mkdir -p $split_output_dir
split -l 100000 $rockyou_path $split_output_dir/rockyou_part_

👀 Link to the official ROCKYOU2024.txt file: https://www.kaggle.com/datasets/bwandowando/original-rockyou2024-text-file-11-parts

🛠️ Installation

To set up Mr. CrackBot AI:
	1.	Clone the repository:

git clone https://github.com/yourusername/mr-crackbot-ai.git
cd mr-crackbot-ai


	2.	Install dependencies:

pip install -r requirements.txt


	3.	Flash the ISO to your SD card and boot your Jetson Nano.
	4.	Split the rockyou2024.txt file (if not automatically split during setup).

⚠️ Disclaimer:
This project is for educational purposes only. Use responsibly and only on networks you own or have permission to test.

🤝 Contributing:
	•	Open issues for bugs or feature requests.
	•	Submit pull requests for new features.




