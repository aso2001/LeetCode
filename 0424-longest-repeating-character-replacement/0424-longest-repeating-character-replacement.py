class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Optimized solution 
        res, mx, L, R = 0, 0, 0, 0
        dd = {}

        while R < len(s):
            c = s[R]
            if c in dd:
                dd[c] += 1
            else:
                dd[c] = 1
            mx = max(mx, dd[c])
            while R - L - mx + 1 > k:
                dd[s[L]] -= 1
                L += 1
            else:
                res = max(res, R - L + 1)
                R += 1 
        return res

    
    def characterReplacement2(self, s: str, k: int) -> int:
        # Sliding window solution using L and R pointers
        res, L, R = 0, 0, 0
        dd = {}

        while R < len(s):
            c = s[R]
            if c in dd:
                dd[c] += 1
            else:
                dd[c] = 1
            while R - L - max(dd.values()) + 1 > k:
                dd[s[L]] -= 1
                L += 1
            else:
                res = max(res, R - L + 1)
                R += 1 
        return res


    def characterReplacement3(self, s: str, k: int) -> int:

        dd = {c:[0, 0] for c in "ABCDEFGHIJKLMNOPRQSTUVWXYZ"}  
        mx = 0

        for i in range(len(s)):
            c = s[i]
            dd[c][0] += 1
            mx = max(mx, dd[c][0] + dd[c][1])
            for d in dd:
                if d != c:
                    if dd[d][1] == k:
                        if dd[d][0] > 0:
                            while s[i - dd[d][0] - dd[d][1]] == d:
                                dd[d][0] -= 1
                        else:
                            dd[d][0] = 0
                    else:
                        dd[d][1] += 1
                        mx = max(mx, dd[d][0] + dd[d][1])
        return mx