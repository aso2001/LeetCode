class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7

        dp = [-1] * (high + 1)

        def dfs(i):
            if i > high:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = 1 if i >= low else 0
            dp[i] += dfs(i + zero) + dfs(i + one)
            return dp[i] % mod

        return dfs(0)