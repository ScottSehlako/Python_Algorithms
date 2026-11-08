"""Binary search: O(log n). Requires sorted input."""

class BinarySearch:
    @staticmethod
    def search(arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1