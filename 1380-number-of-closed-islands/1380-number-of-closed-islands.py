class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            nonlocal flag
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == 1:
                return 0
            elif (i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1) and  grid[i][j] == 0:
                flag = -1
                
            grid[i][j] = 1             
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            if not flag:
                return 1
            return 0

        res = flag = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if grid[i][j]:
                    continue
                res += dfs(i, j)
                flag = 0
        return res