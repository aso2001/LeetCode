class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        n = 0
        while n <= 32:
            if c & (1 << n):
                if (a & (1 << n)) == 0 and (b & (1 << n)) == 0:
                    cnt += 1
            else:
                if a & (1 << n):
                    cnt += 1
                if b & (1 << n):
                    cnt += 1
            n += 1
        return cnt