class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dd = set(dictionary)
        dp = [0]*(n + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                cur = s[start: end + 1]
                if cur in dd:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]