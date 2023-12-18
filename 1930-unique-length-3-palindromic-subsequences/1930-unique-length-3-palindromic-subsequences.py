class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dd = {}
        for i in range(len(s)):
            if s[i] in dd:
                if len(dd[s[i]]) == 2:
                    dd[s[i]][1] = i
                else:
                    dd[s[i]].append(i)
            else:
                dd[s[i]] = [i]

        res = 0
        for d in dd:
            if len(dd[d]) == 1:
                continue
            ee = {}
            for i in range(dd[d][0] + 1, dd[d][1]):
                if s[i] in ee: continue
                ee[s[i]] = 1
            res += len(ee)
        return res