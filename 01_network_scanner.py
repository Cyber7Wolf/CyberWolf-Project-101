#!/usr/bin/env python3
"""🐺 CYBERWOLF NETWORK SCANNER"""
import os
import subprocess

print("\n🐺 CyberWolf Network Scanner")
print("="*50)

target = input("📡 Target IP/Range: ")
print(f"\n🔍 Scanning {target}...")

# Quick scan
os.system(f"nmap -sV --top-ports 100 {target}")

print("\n✅ Scan complete!")
print("🐺 The Wolf Watches. The Wolf Protects.")
