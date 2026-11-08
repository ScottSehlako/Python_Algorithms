"""SHA-256 hashing demo."""

import hashlib

class HashingDemo:
    @staticmethod
    def run():
        print("\n=== HASHING — SHA-256 ===")
        raw = input("Enter text to hash (default: hello): ").strip() or "hello"
        digest = hashlib.sha256(raw.encode()).hexdigest()
        print(f"  Input:  {raw}")
        print(f"  SHA256: {digest}")
        print("   Change even one character completely.")
        print("  That's why hashing secures passwords & verifies data integrity.")