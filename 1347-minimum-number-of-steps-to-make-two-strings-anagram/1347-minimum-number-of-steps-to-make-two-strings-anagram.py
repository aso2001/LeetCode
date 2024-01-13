class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dd = {}
        for c in t:
            if c in dd:
                dd[c] += 1
            else:
                dd[c] = 1
        for c in s:
            if c in dd and dd[c] > 0:
                dd[c] -= 1
        res = 0
        for d in dd:
            res += dd[d]
        return res