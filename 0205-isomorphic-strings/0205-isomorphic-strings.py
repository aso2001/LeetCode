class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        i = 0
        for c in s:
            if c in d1:
                if d1[c] != t[i]:
                    return False
                if t[i] in d2:
                    if d2[t[i]] != c:
                        return False
                else:
                    d2[t[i]] = c
            else:
                if t[i] in d2:
                    if d2[t[i]] != c:
                        return False
                else:
                    d2[t[i]] = c
                d1[c] = t[i]
            i += 1
        return True