class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        lmin = len(min(s))
        res = ""
        for i in range(lmin):
            for ss in s[1:]:
                if s[0][i] != ss[i]: return res
            res += s[0][i]
        return res