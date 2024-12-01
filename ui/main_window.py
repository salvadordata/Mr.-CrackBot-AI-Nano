import tkinter as tk
from tkinter import ttk
from network.scanner import scan_networks
from network.handshake import capture_handshake
from cracking.hashcat_wrapper import crack_password

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Jetson Crack AI - Network Cracking Interface")
        self.root.geometry("800x600")

        # Table to display networks
        self.network_table = ttk.Treeview(self.root, columns=("BSSID", "Channel", "Status"), show="headings")
        self.network_table.heading("BSSID", text="BSSID")
        self.network_table.heading("Channel", text="Channel")
        self.network_table.heading("Status", text="Status")
        self.network_table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Progress Label
        self.progress_label = tk.Label(self.root, text="Progress: 0%")
        self.progress_label.pack(pady=5)

        # Control Buttons
        self.scan_button = tk.Button(self.root, text="Scan Networks", command=self.scan_networks)
        self.scan_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.capture_button = tk.Button(self.root, text="Capture Handshake", command=self.capture_handshake)
        self.capture_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.crack_button = tk.Button(self.root, text="Start Cracking", command=self.start_cracking)
        self.crack_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.networks = []  # Store networks from the scanner
        self.handshake_files = {}  # Map BSSIDs to handshake files

    def scan_networks(self):
        self.networks = scan_networks()
        self.network_table.delete(*self.network_table.get_children())
        for network in self.networks:
            self.network_table.insert("", tk.END, values=(network["bssid"], network["channel"], "Pending"))

    def capture_handshake(self):
        selected = self.network_table.selection()
        if not selected:
            self.progress_label.config(text="No network selected!")
            return
        for sel in selected:
            bssid = self.network_table.item(sel)["values"][0]
            channel = self.network_table.item(sel)["values"][1]
            self.progress_label.config(text=f"Capturing handshake for {bssid}...")
            handshake_file = capture_handshake(bssid, channel)
            self.handshake_files[bssid] = handshake_file
            self.network_table.item(sel, values=(bssid, channel, "Handshake Captured"))

    def start_cracking(self):
        selected = self.network_table.selection()
        if not selected:
            self.progress_label.config(text="No network selected!")
            return
        for sel in selected:
            bssid = self.network_table.item(sel)["values"][0]
            handshake_file = self.handshake_files.get(bssid)
            if not handshake_file:
                self.progress_label.config(text=f"No handshake for {bssid}")
                continue
            self.progress_label.config(text=f"Cracking password for {bssid}...")
            crack_password(handshake_file, "data/wordlists/generated.txt")
            self.network_table.item(sel, values=(bssid, "Cracked", "Password Found"))

    def run(self):
        self.root.mainloop()


# Run the UI
if __name__ == "__main__":
    app = MainWindow()
    app.run()
