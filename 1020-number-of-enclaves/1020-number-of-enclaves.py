class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def dfs(i, j):
            nonlocal flag, res, cnt
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or not grid[i][j]:
                return 0
            elif (i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1) and grid[i][j]:
                flag = -1

            grid[i][j] = 0
            cnt += 1
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
        
        res = cnt = flag = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                if not grid[i][j]:
                    continue
                flag = 0
                dfs(i, j)
                if not flag:
                    res += cnt
                cnt = 0
        return res