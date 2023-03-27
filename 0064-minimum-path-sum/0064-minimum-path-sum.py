class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # DP Solution
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1:
                    if j < len(grid[0]) - 1:
                        grid[i][j] += grid[i][j + 1]
                elif j == len(grid[0]) - 1:
                    grid[i][j] += grid[i + 1][j]
                else:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])
        return grid[0][0]
    
    
    def minPathSum2(self, grid: List[List[int]]) -> int:
        # Recursive solution
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