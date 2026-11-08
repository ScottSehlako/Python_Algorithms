"""Mini blockchain with proof of work."""

import hashlib
import time


class Block:
    def __init__(self, index, data, prev_hash, difficulty=3):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self._mine()

    def _compute_hash(self):
        payload = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}{self.nonce}"
        return hashlib.sha256(payload.encode()).hexdigest()

    def _mine(self):
        target = "0" * self.difficulty
        h = self._compute_hash()
        while not h.startswith(target):
            self.nonce += 1
            h = self._compute_hash()
        return h


class BlockchainDemo:
    @staticmethod
    def run():
        print("\n=== BLOCKCHAIN — Proof of Work ===")
        raw = input("Enter a message for block 1 (default: Alice pays Bob 5): ").strip()
        data = raw or "Alice pays Bob 5"
        difficulty = 3
        print(f"  Mining with difficulty={difficulty} (hash must start with '{'0' * difficulty}')...\n")

        genesis = Block(0, "Genesis", "0" * 64, difficulty)
        start = time.perf_counter()
        block1 = Block(1, data, genesis.hash, difficulty)
        elapsed = time.perf_counter() - start

        print(f"  Block 0 hash: {genesis.hash}")
        print(f"  Block 1 hash: {block1.hash}")
        print(f"  Nonce found:  {block1.nonce}")
        print(f"  Mined in {elapsed:.3f}s")
        print("  That nonce is why Bitcoin consumes energy.")