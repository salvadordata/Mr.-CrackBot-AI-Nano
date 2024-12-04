1   from kivy.app import App
2   from kivy.uix.boxlayout import BoxLayout
3   from kivy.uix.button import Button
4   from kivy.uix.label import Label
5   from kivy.uix.listview import ListView, ListItemButton
6   from kivy.uix.progressbar import ProgressBar
7   from kivy.clock import Clock
8   from network.scanner import scan_networks
9   from network.handshake import capture_handshake
10  from cracking.hashcat_wrapper import crack_password

12  class CrackBotUI(BoxLayout):
13      def __init__(self, **kwargs):
14          super().__init__(orientation="vertical", **kwargs)

16          # Title Label
17          self.title_label = Label(
18              text="Mr. CrackBot AI", font_size="24sp", size_hint=(1, 0.1)
19          )
20          self.add_widget(self.title_label)

22          # Scan Networks Button
23          self.scan_button = Button(
24              text="Scan Networks", size_hint=(1, 0.1), on_press=self.scan_networks
25          )
26          self.add_widget(self.scan_button)

28          # Network List
29          self.network_list_label = Label(
30              text="Networks Found:", size_hint=(1, 0.1)
31          )
32          self.add_widget(self.network_list_label)
33          self.network_list = ListView(size_hint=(1, 0.3))
34          self.add_widget(self.network_list)

36          # Capture Handshake Button
37          self.capture_button = Button(
38              text="Capture Handshake", size_hint=(1, 0.1), on_press=self.capture_handshake
39          )
40          self.add_widget(self.capture_button)

42          # Start Cracking Button
43          self.crack_button = Button(
44              text="Start Cracking", size_hint=(1, 0.1), on_press=self.start_cracking
45          )
46          self.add_widget(self.crack_button)

48          # Progress Bar
49          self.progress_label = Label(
50              text="Progress:", size_hint=(1, 0.1)
51          )
52          self.add_widget(self.progress_label)
53          self.progress_bar = ProgressBar(max=100, size_hint=(1, 0.1))
54          self.add_widget(self.progress_bar)

56          # Log Output
57          self.log_label = Label(
58              text="Logs:", size_hint=(1, 0.1)
59          )
60          self.add_widget(self.log_label)
61          self.log_output = Label(
62              text="", size_hint=(1, 0.3), halign="left", valign="top"
63          )
64          self.log_output.bind(size=self.log_output.setter("text_size"))
65          self.add_widget(self.log_output)

67      def scan_networks(self, instance):
68          """Scan for networks and display them in the list."""
69          self.log("Scanning for networks...")
70          networks = scan_networks()
71          if networks:
72              # Display networks in the list
73              self.network_list.adapter.data.clear()
74              for network in networks:
75                  self.network_list.adapter.data.append(f"{network['ssid']} ({network['bssid']})")
76              self.network_list._trigger_reset_populate()
77          else:
78              self.log("No networks found.")

80      def capture_handshake(self, instance):
81          """Capture the handshake for the selected network."""
82          selected_network = self.get_selected_network()
83          if selected_network:
84              self.log(f"Capturing handshake for {selected_network}...")
85              handshake_file = capture_handshake(selected_network["bssid"], selected_network["channel"])
86              self.log(f"Handshake saved to: {handshake_file}")
87          else:
88              self.log("Please select a network first.")

90      def start_cracking(self, instance):
91          """Start cracking the password for the selected network."""
92          selected_network = self.get_selected_network()
93          if selected_network:
94              self.log(f"Starting password cracking for {selected_network}...")
95              handshake_file = f"data/captures/{selected_network['bssid']}-01.cap"
96              crack_password(
97                  handshake_file, "data/wordlists/generated.txt", progress_callback=self.update_progress
98              )
99          else:
100             self.log("Please select a network first.")

