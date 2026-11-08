"""Race linear vs binary search on the same array."""

import os
import time

from ..searching import LinearSearch, BinarySearch


def _clear():
    os.system("cls" if os.name == "nt" else "clear")


def race_searches(values, target):
    _clear()
    print("=" * 60)
    print(f" SEARCH RACE — target = {target}")
    print("=" * 60)

    sorted_values = sorted(values)
    print(f"  Sorted input: {sorted_values if len(sorted_values) <= 20 else sorted_values[:20] + ['...']}\n")

    t0 = time.perf_counter()
    li = LinearSearch.search(sorted_values, target)
    t_lin = time.perf_counter() - t0

    t0 = time.perf_counter()
    bi = BinarySearch.search(sorted_values, target)
    t_bin = time.perf_counter() - t0

    print(f"  Linear search → index {li:>3}  ({t_lin * 1000:.4f} ms)")
    print(f"  Binary search → index {bi:>3}  ({t_bin * 1000:.4f} ms)")

    if t_bin > 0:
        print(f"\n  Binary is ~{t_lin / t_bin:.1f}× faster (only works on sorted data)")