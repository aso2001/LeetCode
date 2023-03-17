class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, dt, ds = "", {}, {}

        for c in t:
            if c in dt:
                dt[c] += 1
            else:
                dt[c] = 1
                ds[c] = 0
        
        L, R, minr, res = 0, 1, 10**5, ""

        need = len(dt)
        have = 0

        for R in range(len(s)):
            c = s[R]
            if c in dt:
                ds[c] += 1
                if ds[c] == dt[c]:
                    have += 1
                
                while have == need:
                    if R - L < minr:
                        minr = R - L
                        res = s[L:R + 1]
                    if s[L] in dt:
                        ds[s[L]] -= 1
                        if ds[s[L]] < dt[s[L]]:
                            have -= 1
                    L += 1
        return res