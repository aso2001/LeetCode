class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dd = {}
        res = -1
        for i in range(len(s)):
            if s[i] in dd:
                res = max(res, i - dd[s[i]] - 1)
            else:
                dd[s[i]] = i
        return res