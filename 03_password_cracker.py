#!/usr/bin/env python3
"""🐺 CYBERWOLF PASSWORD CRACKER"""
import hashlib

print("\n🐺 CyberWolf Password Cracker")
print("="*50)

hash_input = input("🔐 Enter hash: ")

# Identify hash type
length = len(hash_input)
if length == 32:
    hash_type = "MD5"
elif length == 40:
    hash_type = "SHA-1"
elif length == 64:
    hash_type = "SHA-256"
else:
    hash_type = "Unknown"

print(f"📊 Hash type: {hash_type}")
print("💡 Try using hashcat or john for cracking")

print("\n🐺 The Wolf Watches. The Wolf Protects.")
