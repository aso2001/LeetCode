class Solution:
    def minimumLength(self, s: str) -> int:
        L, R = 0, len(s) - 1
        while L < R and s[L] == s[R]:
            prev = s[L]
            while L <= R and s[L] == prev:
                L += 1
            while L <= R and s[R] == prev:
                R -= 1
        return R - L + 1