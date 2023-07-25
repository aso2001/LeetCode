class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        L, R = 0, len(arr) - 1
        while L <= R:
            mid = (L + R) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                L = mid + 1
            elif arr[mid - 1] > arr[mid]:
                R = mid - 1