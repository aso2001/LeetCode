class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        moves = [(-1,0), (1,0), (0,-1), (0,1)]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    for m in moves:
                        if i + m[0] < 0 or i + m[0] == len(grid) or j + m[1] < 0 or j + m[1] == len(grid[0]) or grid[i + m[0]][j + m[1]] == 0:
                            res += 1
        return res