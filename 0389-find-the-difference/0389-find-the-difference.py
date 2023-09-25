class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ds = {}
        dt = {}

        for c in s:
            if c in ds:
                ds[c] += 1
            else:
                ds[c] = 1
        for c in t:
            if c in dt:
                dt[c] += 1
            else:
                dt[c] = 1
        for c in dt:
            if c not in ds or ds[c] != dt[c]:
                return c      