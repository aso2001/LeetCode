class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot, rot2, org  = set(), set(), set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rot.add((i, j))
                if grid[i][j] == 2 or grid[i][j] == 1:
                    org.add((i, j))
        
        rot2 = rot.copy()

        def bfs(i, j, lev, rot2):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] != 1:
                return
            grid[i][j] = 2
            lev.add((i, j))
            rot2.add((i, j))

        moves = {(-1, 0), (1, 0), (0, -1), (0, 1)}
        cnt = 0
        while True:
            lev = set()
            for nn in rot:
                for mm in moves:
                    bfs(nn[0] + mm[0], nn[1] + mm[1], lev, rot2)
            if lev != set():
                cnt += 1
                rot = lev
            else:
                break
        if rot2 == org:
            return cnt
        return -1

