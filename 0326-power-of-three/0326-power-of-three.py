class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True
        while n >= 9:
            n /= 3
        return n == 3