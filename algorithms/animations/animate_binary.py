"""Live binary search animation."""

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


def animate_binary_search(sorted_arr, target, delay=0.5):
    low, high = 0, len(sorted_arr) - 1
    while low <= high:
        _clear()
        mid = (low + high) // 2
        print(f"  BINARY SEARCH target: {target}")
        print(f"  low={low}  mid={mid}  high={high}\n")
        _print_array(sorted_arr, highlight=mid, title=f"checking index {mid} = {sorted_arr[mid]}")
        if sorted_arr[mid] == target:
            print(f"\n  Found {target} at index {mid}")
            return
        if sorted_arr[mid] < target:
            print(f"\n  → going RIGHT (halving)")
            low = mid + 1
        else:
            print(f"\n  → going LEFT (halving)")
            high = mid - 1
        time.sleep(delay)
    print(f"\n  {target} not found!!!")