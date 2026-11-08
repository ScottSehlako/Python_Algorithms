"""Queue(First In, First Out)."""

from collections import deque

class QueueDemo:
    def __init__(self, items=None):
        self.items = deque(items or [])

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"Queue({list(self.items)})"

    @staticmethod
    def run():
        print("\n=== QUEUE (FIFO) ===")
        raw = input("Enter items separated by commas (default Alice,Bob,Charlie): ").strip()
        q = QueueDemo(raw.split(",") if raw else ["Alice", "Bob", "Charlie"])
        print(f"  Initial: {q}")
        while q:
            print(f"  dequeue(): {q.dequeue()}  | remaining: {q}")