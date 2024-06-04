class Solution:
    def longestPalindrome(self, s: str) -> int:
        dd = defaultdict(int)
        for c in s:
            dd[c] += 1
        res, flag = 0, 0
        for d in dd:
            if dd[d]%2 and flag == 0:
                res += dd[d]
                flag = 1
            elif dd[d] > 1:
                res += 2*(dd[d]//2)
        return res