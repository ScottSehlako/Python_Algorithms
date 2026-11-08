"""Counting sort: O(n + k). Non-negative integers only."""

class CountingSort:
    @staticmethod
    def sort(arr):
        if not arr:
            return []
        max_v = max(arr)
        counts = [0] * (max_v + 1)
        for v in arr:
            counts[v] += 1
        out = []
        for i, c in enumerate(counts):
            out.extend([i] * c)
        return out