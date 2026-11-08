"""Quick sort: O(n log n) average."""

class QuickSort:
    @staticmethod
    def sort(arr):
        if len(arr) <= 1:
            return arr[:]
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return QuickSort.sort(left) + mid + QuickSort.sort(right)