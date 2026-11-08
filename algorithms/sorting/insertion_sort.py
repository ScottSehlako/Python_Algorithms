"""Insertion sort: O(n^2), fast on nearly-sorted data."""

class InsertionSort:
    @staticmethod
    def sort(arr):
        a = arr[:]
        for i in range(1, len(a)):
            key = a[i]
            j = i - 1
            while j >= 0 and a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            a[j + 1] = key
        return a