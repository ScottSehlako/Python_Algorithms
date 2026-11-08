"""Heap sort: O(n log n) using heapq."""

import heapq

class HeapSort:
    @staticmethod
    def sort(arr):
        h = arr[:]
        heapq.heapify(h)
        return [heapq.heappop(h) for _ in range(len(h))]