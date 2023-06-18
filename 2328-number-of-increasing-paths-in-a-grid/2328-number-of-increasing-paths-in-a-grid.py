class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        sorted_grid = [(i, j) for i in range(len(grid)) for j in range(len(grid[0]))]
        dp = [[1]*len(grid[0]) for _ in range(len(grid))]
        sorted_grid.sort(key = lambda x: grid[x[0]][x[1]])
        moves = {(-1,0), (1,0), (0,-1), (0,1)}

        for i, j in sorted_grid:
            for m in moves:
                if i + m[0] >= 0 and i + m[0] < len(grid) and j + m[1] >= 0 and j + m[1] < len(grid[0]) and grid[i][j] < grid[i + m[0]][j + m[1]]:
                    dp[i + m[0]][j + m[1]] += dp[i][j]
                    dp[i + m[0]][j + m[1]] %= mod

        return sum(sum(r)%mod for r in dp)%mod