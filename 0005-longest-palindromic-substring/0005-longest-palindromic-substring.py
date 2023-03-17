class Solution:
    def longestPalindrome(self, s: str) -> str:

        pmax = 0
        for i in range(len(s)):
            L, R = i, i + 1  # even length palindrom
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if pmax < R - L + 1:
                    pmax = R - L + 1
                    mpal = s[L:R + 1]
                R += 1
                L -= 1
            
            L, R = i, i  # odd length palindrom
            while L >= 0 and R < len(s) and s[L] == s[R]:
                if pmax < R - L + 1:
                    pmax = R - L + 1
                    mpal = s[L:R + 1]
                R += 1
                L -= 1
        return mpal