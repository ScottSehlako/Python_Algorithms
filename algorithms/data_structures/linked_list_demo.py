"""Singly linked list with append, delete and display."""

class _Node:
    __slots__ = ("value", "next")

    def __init__(self, value):
        self.value = value
        self.next = None

"""////////////////////////////// +END CLASS+ ///////////////////////////////////////"""

class LinkedList:
    def __init__(self, items=None):
        self.head = None
        for v in (items or []):
            self.append(v)

    def append(self, value):
        new = _Node(value)
        if not self.head:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new

    def delete(self, value):
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        cur = self.head
        while cur.next and cur.next.value != value:
            cur = cur.next
        if cur.next:
            cur.next = cur.next.next
            return True
        return False

    def to_list(self):
        out, cur = [], self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

    @staticmethod
    def run():
        print("\n=== LINKED LIST ===")
        raw = input("Enter initial values (default 10,20,30,40): ").strip()
        ll = LinkedList([int(x) for x in raw.split(",")] if raw else [10, 20, 30, 40])
        print(f"  List: {ll.to_list()}")
        while True:
            target = input("  Delete value (blank to quit): ").strip()
            if not target:
                break
            try:
                ok = ll.delete(int(target))
                print(f"  delete({target}) → {ok}  | list: {ll.to_list()}")
            except ValueError:
                print("  Please enter a number.")