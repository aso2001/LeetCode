class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        dp = [[math.inf]*len(grid[0]) for _ in range(len(grid))]

        def dfs(i, j):
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]
            if dp[i][j] != math.inf:
                return dp[i][j]
            if i == len(grid) - 1:
                return grid[i][j] + dfs(i, j + 1)
            if j == len(grid[0]) - 1:
                return grid[i][j] + dfs(i + 1, j)
            
            if i < len(grid) - 1 and j < len(grid[0]) - 1:
                dp[i][j] = grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))
                return dp[i][j]
        return dfs(0,0)