"""Bubble sort: O(n^2)."""

class BubbleSort:
    @staticmethod
    def sort(arr):
        a = arr[:]
        n = len(a)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True
            if not swapped:
                break
        return a