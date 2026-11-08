"""Live bubble sort animation."""

import os
import time


def _clear():
    os.system("cls" if os.name == "nt" else "clear")


def _print_array(values, highlight=None, title=""):
    if title:
        print(f"  {title}")
    mx = max(values) or 1
    for i, v in enumerate(values):
        bar = "█" * max(1, int(v / mx * 40))
        marker = " ◀" if i == highlight else ""
        print(f"   {i:>2}: {bar} {v}{marker}")


def animate_bubble(values, delay=0.15):
    a = values[:]
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            _clear()
            print(f"  BUBBLE SORT — pass {i + 1}, comparing index {j} vs {j + 1}\n")
            _print_array(a, highlight=j, title=f"comparing {a[j]} and {a[j + 1]}")
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            time.sleep(delay)
    _clear()
    print(" SORTED!\n")
    _print_array(a)