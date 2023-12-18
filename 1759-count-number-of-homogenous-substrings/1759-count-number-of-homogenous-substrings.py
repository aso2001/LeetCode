class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        res, cnt = 0, 0
        prev = 'X'
        for c in s:
            if c != prev:
                res = (res + cnt*(cnt + 1)//2) % mod
                cnt = 1
            else:
                cnt += 1
            prev = c
        res = (res + cnt*(cnt + 1)//2) % mod
        return res