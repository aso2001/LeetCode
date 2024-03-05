class Solution:
    def minimumLength(self, s: str) -> int:
        res, L, R = len(s), 0, len(s) - 1
        while L < R:
            if s[L] == s[R]:
                prevL = s[L]
                prevR = s[R]
                res -= 2
                flagL = 0
                flagR = 0
                while L < R:
                    if L + 1 < R and s[L + 1] == prevL:
                        L += 1
                        res -= 1
                    elif flagR:
                        break
                    else:
                        flagL = 1
                    if R - 1 > L and s[R - 1] == prevR:
                        R -= 1
                        res -= 1
                    elif flagL:
                        break
                    else:
                        flagR = 1
                L += 1
                R -= 1
            else:
                break
        return res