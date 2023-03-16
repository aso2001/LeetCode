class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        pfx = [[0]*(len(grid[0]) + 2) for _ in range(2)]
        for i in range(1, len(grid[0])):
            pfx[1][i] = pfx[1][i - 1] + grid[1][i - 1]
        for i in range(len(grid[0]) - 1, -1, -1):
            pfx[0][i + 1] = pfx[0][i + 2] + grid[0][i]
            
        res = math.inf
        for i in range(len(grid[0]) + 1):
            res = min(res, max(pfx[0][i + 1], pfx[1][i - 1]))
        return res