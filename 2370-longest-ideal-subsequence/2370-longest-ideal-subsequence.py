class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0]*26
        for i in range(len(s)):
            tmp = 0
            for prev in range(26):
                if abs(ord(s[i]) - ord('a') - prev) <= k:
                    tmp = max(tmp, dp[prev])
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], tmp + 1)
        return max(dp)