class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        moves = [(-1,0),(1,0),(0,-1),(0,1)]
        ones = []
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ones.append((i, j))

        cnt = 0
        for cur in ones:
            if grid[cur[0]][cur[1]] == '0': continue
            q.append(cur)
            while q:
                cur = q.popleft()
                grid[cur[0]][cur[1]] = '0'
                for m in moves:
                    if cur[0] + m[0] >= 0 and cur[0] + m[0] < len(grid) and cur[1] + m[1] >= 0 and cur[1] + m[1] < len(grid[0]) and grid[cur[0] + m[0]][cur[1] + m[1]] == '1':
                        q.append((cur[0] + m[0], cur[1] + m[1]))
                        grid[cur[0] + m[0]][cur[1] + m[1]] = '0'
            cnt += 1
        return cnt
    

    def numIslands3(self, grid: List[List[str]]) -> int:

        res = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return 0
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            return 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += dfs(i,j)
        return res

    
    def numIslands2(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            if 0 > i or i == len(grid) or 0 > j or j == len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
        return cnt