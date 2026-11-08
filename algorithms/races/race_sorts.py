"""Race all sorting algorithms on the same array."""

import os
import time

from ..sorting import (
    BubbleSort, InsertionSort, SelectionSort,
    MergeSort, QuickSort, HeapSort,
)


SORT_ALGORITHMS = {
    "Bubble":    BubbleSort,
    "Insertion": InsertionSort,
    "Selection": SelectionSort,
    "Merge":     MergeSort,
    "Quick":     QuickSort,
    "Heap":      HeapSort,
}


def _clear():
    os.system("cls" if os.name == "nt" else "clear")


def race_sorts(values):
    _clear()
    print("=" * 60)
    print(f"🏁 SORT RACE — {len(values)} elements")
    print("=" * 60)
    print(f"  Input: {values if len(values) <= 15 else values[:15] + ['...']}\n")

    results = []
    expected = sorted(values)

    for name, alg in SORT_ALGORITHMS.items():
        arr = values[:]
        t0 = time.perf_counter()
        output = alg.sort(arr)
        elapsed = time.perf_counter() - t0
        assert output == expected, f"{name} produced wrong output!"
        results.append((name, elapsed, output))
        print(f"  {name:<10} {elapsed * 1000:>8.2f} ms  ")

    t0 = time.perf_counter()
    builtin = sorted(values[:])
    elapsed = time.perf_counter() - t0
    assert builtin == expected
    results.append(("Timsort*", elapsed, builtin))
    print(f"  {'Timsort*':<10} {elapsed * 1000:>8.2f} ms   (*=Python built-in)")

    print("\n  Relative speed (shorter is better):")
    worst = max(r[1] for r in results) or 1e-9
    for name, t, _ in sorted(results, key=lambda x: x[1]):
        bar = "█" * max(1, int(t / worst * 40))
        print(f"  {name:<10} {bar} {t * 1000:.2f} ms")