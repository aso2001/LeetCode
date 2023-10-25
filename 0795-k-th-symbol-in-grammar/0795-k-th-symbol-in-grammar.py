class Solution:
    def rec(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        tot = 2**(n - 1)
        half = tot//2
        if k > half:
            return 1 - self.rec(n, k - half)
        return self.rec(n - 1, k)

    def kthGrammar(self, n: int, k: int) -> int:
        return self.rec(n, k)