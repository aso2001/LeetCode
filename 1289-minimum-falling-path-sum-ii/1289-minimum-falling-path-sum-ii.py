class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0]*n for _ in range(n)]

        dp[0] = grid[0]
        for j in range(1, n):
            tmp = dp[j - 1]
            for i in range(n):
                dp[j][i] = grid[j][i] + min(min(tmp[:i]) if i > 0 else math.inf, min(tmp[i+1:]) if i < n - 1 else math.inf)
        return min(dp[n - 1])