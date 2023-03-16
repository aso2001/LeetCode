class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            L, R = i, i             # even number palindrome
            while L >= 0 and R <= len(s) - 1 and s[L] == s[R]:
                cnt += 1
                L, R  = L - 1, R + 1
        for i in range(len(s) - 1):
            L, R = i , i + 1        # odd number palindrome
            while L >= 0 and R <= len(s) - 1 and s[L] == s[R]:
                cnt += 1
                L, R = L - 1, R + 1
        return cnt