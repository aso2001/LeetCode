class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        if n == 1: return 0
        while n > 2:
            if not n % 2:
                res += n // 2
                n //= 2
            else:
                res += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return res + 1