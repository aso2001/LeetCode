class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        L, R = 0, len(arr) - 1

        while L <= R:
            mid = (L + R) // 2
            if arr[mid] - mid - 1 >= k:
                R = mid - 1
            elif arr[mid] - mid - 1 < k:
                L = mid + 1
        return R + k + 1

    def findKthPositive2(self, arr: List[int], k: int) -> int:
        diff = [0]*len(arr)
        diff[0] = arr[0] - 1
        for i in range(1, len(arr)):
            diff[i] = arr[i] - arr[i - 1] - 1
        s = 0
        for i in range(len(arr)):
            s += diff[i]
            if s >= k:
                imax = i
                break
            imax = i + 1
        res = imax + k
        return res