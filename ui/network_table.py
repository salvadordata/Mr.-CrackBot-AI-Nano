from tkinter import ttk

class NetworkTable:
    def __init__(self, parent):
        self.tree = ttk.Treeview(parent, columns=("BSSID", "Channel", "Status"), show="headings")
        self.tree.heading("BSSID", text="BSSID")
        self.tree.heading("Channel", text="Channel")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill="both", expand=True)
    
    def update_table(self, networks):
        self.tree.delete(*self.tree.get_children())
        for network in networks:
            self.tree.insert("", "end", values=(network["bssid"], network["channel"], "Pending"))

    def update_status(self, bssid, status):
        for item in self.tree.get_children():
            if self.tree.item(item, "values")[0] == bssid:
                current_values = self.tree.item(item, "values")
                self.tree.item(item, values=(current_values[0], current_values[1], status))
