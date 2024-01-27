class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        prev = [0] * (k + 1)
        prev[0] = 1

        for N in range(1, n + 1):
            cur = [0] * (k + 1)
            tot = 0 # sliding window
            for K in range(0, k + 1):
                if K >= N:
                    tot -= prev[K - N]
                tot = (tot + prev[K]) % mod
                cur[K] = tot
            prev = cur
        return prev[K]

# TLE solution
    def kInversePairs2(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[0]*(k + 1) for _ in range(n + 1)]

        def dfs(n, k):
            if k < 0:
                return 0
            if not n:
                return 1 if not k else 0
            if dp[n][k]:
                return dp[n][k]
            for i in range(n):
                dp[n][k] = (dp[n][k] + dfs(n - 1, k - i)) % mod
            return dp[n][k]

        return dfs(n, k)