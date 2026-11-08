"""Quick smoke test — run with:  python test_smoke.py"""

from algorithms.sorting import (
    BubbleSort, InsertionSort, SelectionSort,
    MergeSort, QuickSort, HeapSort, CountingSort,
)
from algorithms.searching import LinearSearch, BinarySearch


def test_all_sorts():
    test_cases = [[], [1], [3, 1, 2], [5, 2, 9, 1, 7, 3, 8, 4, 6, 0], [1, 1, 1, 1]]
    algorithms = [BubbleSort, InsertionSort, SelectionSort,
                  MergeSort, QuickSort, HeapSort, CountingSort]
    for alg in algorithms:
        for case in test_cases:
            assert alg.sort(case) == sorted(case), f"{alg.__name__} failed on {case}"
    print(f"✅ All {len(algorithms)} sort algorithms pass {len(test_cases)} cases")


def test_searches():
    arr = sorted([5, 2, 9, 1, 7, 3])
    for target in arr + [99]:
        expected = arr.index(target) if target in arr else -1
        assert LinearSearch.search(arr, target) == expected
        assert BinarySearch.search(arr, target) == expected
    print("✅ Both search algorithms correct")


if __name__ == "__main__":
    test_all_sorts()
    test_searches()
    print("\n🎉 All smoke tests passed")
