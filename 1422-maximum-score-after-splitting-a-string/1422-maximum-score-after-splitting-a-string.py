class Solution:
    def maxScore(self, s: str) -> int:
        pfx = [0]*len(s)
        pst = [0]*len(s)
        pfx[0] = 1 if s[0] == '0' else 0
        pst[-1] = 1 if s[-1] == '1' else 0
        for i in range(1, len(s)):
            pfx[i] = pfx[i - 1] + (1 if s[i] == '0' else 0)
        for i in range(len(s) - 2, -1, -1):
            pst[i] = pst[i + 1] + (1 if s[i] == '1' else 0)
        res = 0
        for i in range(len(s) - 1):
            res = max(res, pfx[i] + pst[i + 1])
        return res