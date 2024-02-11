class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = {}
        moves = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
        def dfs(r, c1, c2):
            if c1 == c2 or min(c1,c2) < 0 or max(c1,c2) == len(grid[0]):
                return 0
            if r == len(grid) - 1:
                return grid[r][c1] + grid[r][c2]
            if (r, c1, c2)  in dp:
                return dp[(r, c1, c2)]
            res = - math.inf
            for m in moves:
                # if c1 + m[0] < 0 or c2 + m[1] < 0 or c1 + m[0] == c2 + m[1] or c1 + m[0] == len(grid[0]) or c2 + m[1] == len(grid[0]): 
                #     continue
                res = max(res, grid[r][c1] + grid[r][c2] + dfs(r + 1, c1 + m[0], c2 + m[1]))
            dp[(r, c1, c2)] = res
            return dp[(r, c1, c2)]

        return dfs(0, 0, len(grid[0]) - 1)