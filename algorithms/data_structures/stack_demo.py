"""Stack(Last In, First Out)."""

class StackDemo:
    def __init__(self, items=None):
        self.items = list(items or [])

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise IndexError("Stack is empty")
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"Stack({self.items})"

    @staticmethod
    def run():
        print("\n=== STACK (LIFO) ===")
        raw = input("Enter items separated by commas (default A,B,C): ").strip()
        stack = StackDemo(raw.split(",") if raw else ["A", "B", "C"])
        print(f"  Initial: {stack}")
        while stack:
            print(f"  pop(): {stack.pop()}  | remaining: {stack}")