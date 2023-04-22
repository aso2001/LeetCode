class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[[0]*(minProfit + 1) for _ in range(n + 1)] for _ in range(len(group) + 1)]
        for m in range(n + 1):
            dp[len(group)][m][0] = 1

        for i in range(len(group) - 1, -1, -1):
            for m in range(n + 1):
                for p in range(minProfit + 1):
                    dp[i][m][p] = dp[i + 1][m][p] 
                    if group[i] <= m:
                        dp[i][m][p] += dp[i + 1][m - group[i]][max(0, p - profit[i])]
                    dp[i][m][p] %= 10**9+7

        return dp[0][n][minProfit] 