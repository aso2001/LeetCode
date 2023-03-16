class Solution:
    def firstUniqChar(self, s: str) -> int:
        dd = {}
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if idx in dd:
                dd[idx] = len(s)
                continue
            else:
                dd[idx] = i
        return -1 if min(dd.values()) == len(s) else min(dd.values())