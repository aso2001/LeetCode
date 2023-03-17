class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        L, R = 0, x//2
        while L < R:
            mid = (R + L)//2
            if mid*mid <= x:
                L = mid + 1
            else:
                R = mid - 1
        return L - 1 if L*L > x else L