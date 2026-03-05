class Solution:
    def minOperations(self, s: str) -> int:
        c0, c1 = 0, 0
        for i in range(len(s)):
            if i % 2:
                if s[i] == '0':
                    c0 += 1
            else:
                if s[i] == '1':
                    c1 += 1
        res = min(c0 + c1, len(s) - c0 - c1)
        return res