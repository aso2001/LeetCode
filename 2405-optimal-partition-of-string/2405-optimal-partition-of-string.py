class Solution:
    def partitionString(self, s: str) -> int:
        cnt, i = 1, 1
        d ={s[0]:1}

        while i < len(s):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                cnt += 1
                d = {s[i]:1}
            i += 1
        return cnt     