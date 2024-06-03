class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        L, R = 0, 0
        while L < len(s) and R < len(t):
            if s[L] == t[R]:
                R += 1
            L += 1
        return len(t) - R