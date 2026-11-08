"""Regex demonstrations."""

import re

class RegexDemo:
    @staticmethod
    def run():
        print("\n=== REGEX — Pattern Matching ===")
        raw = input("Enter text (default: email me at alice@example.com on 2024-03-22): ").strip()
        text = raw or "email me at alice@example.com on 2024-03-22"

        emails = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)
        dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)

        print(f"  Emails: {emails or '—'}")
        print(f"  Dates : {dates or '—'}")
        print(f"  Digits redacted: {re.sub(r'\d', 'X', text)}")