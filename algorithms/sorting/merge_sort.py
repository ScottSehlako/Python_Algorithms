"""Merge sort: O(n log n)."""

class MergeSort:
    @staticmethod
    def _merge(l, r):
        out = []
        i = j = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                out.append(l[i]); i += 1
            else:
                out.append(r[j]); j += 1
        out.extend(l[i:])
        out.extend(r[j:])
        return out

    @classmethod
    def sort(cls, arr):
        if len(arr) <= 1:
            return arr[:]
        mid = len(arr) // 2
        return cls._merge(cls.sort(arr[:mid]), cls.sort(arr[mid:]))