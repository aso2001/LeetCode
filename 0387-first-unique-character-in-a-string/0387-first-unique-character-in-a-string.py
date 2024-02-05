class Solution:
    def firstUniqChar(self, s: str) -> int:
        dd = {}
        for i in range(len(s)):
            if s[i] in dd:
                dd[s[i]] = 10**6
            else:
                dd[s[i]] = i
        return min(dd.values()) if min(dd.values()) <= 10**5 else -1

    def firstUniqChar2(self, s: str) -> int:
        dd = {}
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if idx in dd:
                dd[idx] = len(s)
                continue
            else:
                dd[idx] = i
        return -1 if min(dd.values()) == len(s) else min(dd.values())