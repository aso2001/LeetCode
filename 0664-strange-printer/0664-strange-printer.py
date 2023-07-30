class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[n]*n for _ in range(n)]
        for length in range(1, n + 1):
            for L in range(n - length + 1):
                R = L + length - 1
                j = -1
                for i in range(L, R):
                    if s[i] != s[R] and j == -1:
                        j = i
                    if j != -1:
                        dp[L][R] = min(dp[L][R], 1 + dp[j][i] + dp[i + 1][R])
        
                if j == -1:
                    dp[L][R] = 0

        return dp[0][n - 1] + 1