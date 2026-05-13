#!/usr/bin/env python3
"""🐺 CYBERWOLF WEB SCANNER"""
import requests

print("\n🐺 CyberWolf Web Vulnerability Scanner")
print("="*50)

url = input("🌐 Target URL: ")

print(f"\n🔍 Testing {url}...")

try:
    response = requests.get(url, timeout=5)
    print(f"✅ Status: {response.status_code}")
    print(f"📊 Server: {response.headers.get('Server', 'Unknown')}")
except:
    print("❌ Could not connect")

print("\n✅ Scan complete!")
print("🐺 The Wolf Watches. The Wolf Protects.")
