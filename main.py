"""Entry point: run this file:  python main.py"""

import os
import random

from algorithms.data_structures import StackDemo, QueueDemo, LinkedList, HashMapDemo
from algorithms.searching import LinearSearch, BinarySearch  # noqa: F401  (used in races)
from algorithms.cryptography import HashingDemo, BlockchainDemo
from algorithms.regex import RegexDemo
from algorithms.recursion import Fibonacci
from algorithms.graphs import Dijkstra, BFS, DFS, AStar
from algorithms.animations import animate_bubble, animate_binary_search
from algorithms.races import race_sorts, race_searches


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def ask_array(default_size=15):
    raw = input(
        f"Enter numbers separated by commas, or 'random' "
        f"(default: random {default_size}): "
    ).strip().lower()
    if not raw or raw == "random":
        return [random.randint(1, 100) for _ in range(default_size)]
    try:
        return [int(x.strip()) for x in raw.split(",") if x.strip()]
    except ValueError:
        print("  Invalid input — using defaults.")
        return [random.randint(1, 100) for _ in range(default_size)]


def menu():
    options = [
        ("Stack (interactive)",             StackDemo.run),
        ("Queue (interactive)",             QueueDemo.run),
        ("Linked List (interactive)",       LinkedList.run),
        ("Hash Map (word counter)",         HashMapDemo.run),
        ("Hashing (SHA-256)",               HashingDemo.run),
        ("Blockchain (proof of work)",      BlockchainDemo.run),
        ("Fibonacci (recursion vs memo)",   Fibonacci.run),
        ("Regex (emails/dates/redaction)",  RegexDemo.run),
        ("Dijkstra (shortest path)",        Dijkstra.run),
        ("BFS (breadth-first)",             BFS.run),
        ("DFS (depth-first)",               DFS.run),
        ("A* (heuristic search)",           AStar.run),
        (" Animate: Bubble Sort",          lambda: animate_bubble(ask_array(10)[:10])),
        (" Animate: Binary Search",        lambda: animate_binary_search(
                                                sorted(ask_array(10)[:10]),
                                                int(input("Target: ") or 50))),
        (" Race: Sorts",                   lambda: race_sorts(ask_array(30))),
        (" Race: Searches",                lambda: race_searches(
                                                ask_array(30),
                                                int(input("Search target: ") or 50))),
    ]

    while True:
        clear()
        print("\n PYTHON ALGORITHMS — MAIN MENU")
        print("=" * 60)
        for i, (label, _) in enumerate(options, 1):
            print(f"  {i:>2}. {label}")
        print("   0. Quit")

        choice = input("\nChoose: ").strip()
        if choice == "0":
            break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                clear()
                options[idx][1]()
                input("\nPress ENTER to return to menu...")
            else:
                print("  Out of range.")
        except ValueError:
            print("  Not a number.")
        except KeyboardInterrupt:
            print("\n  Interrupted.")


if __name__ == "__main__":
    menu()