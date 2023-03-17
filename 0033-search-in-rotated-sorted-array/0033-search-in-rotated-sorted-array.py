class Solution:
    def search(self, n: List[int], t: int) -> int:
        L, R = 0, len(n) - 1
        while L <= R:
            mid = (L + R) // 2
            if t == n[mid]: return mid
            if n[L] <= n[mid]:
                if n[L] <= t <= n[mid]: R = mid - 1
                else: L = mid + 1
            else:
                if n[mid] <= t <= n[R]: L = mid + 1
                else: R = mid - 1
        return -1