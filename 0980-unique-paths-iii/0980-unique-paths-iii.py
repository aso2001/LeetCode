class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        tot = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not grid[i][j]: 
                    tot += 1
                elif grid[i][j] == 1:
                    i0 = i
                    j0 = j
                    
        cnt, res = 0, 0
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def backtrack(i, j):
            nonlocal res, cnt
            for m in moves:
                if 0 <= i + m[0] < len(grid) and 0 <= j + m[1] < len(grid[0]) and grid[i + m[0]][j + m[1]] != -1 and grid[i + m[0]][j + m[1]] != 3 and grid[i + m[0]][j + m[1]] != 1:
                    if grid[i + m[0]][j + m[1]] == 2:
                        if cnt == tot:
                            res += 1
                            continue
                        else:
                            continue
                    cnt += 1
                    grid[i + m[0]][j + m[1]] = 3
                    backtrack(i + m[0], j + m[1])
                    grid[i + m[0]][j + m[1]] = 0
                    cnt -= 1

        backtrack(i0, j0)
        return res