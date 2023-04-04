class Solution:
    def partitionString(self, s: str) -> int:
        cnt, i = 1, 1
        d = set(s[0])

        while i < len(s):
            if s[i] not in d:
                d.add(s[i])
            else:
                cnt += 1
                d = set(s[i])
            i += 1
        return cnt     