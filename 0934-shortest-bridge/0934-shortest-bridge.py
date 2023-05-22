class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        grp1 = {}
        grp2 = {}
        ones = {}
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    ones[(i, j)] = 1
        i, j = list(ones.keys())[0]
        grp1[(i, j)] = 1
        q = deque()
        pair = (i, j)
        q.append(pair)
        visited = [[0]*len(grid[0]) for _ in range(len(grid))]
        moves = {(-1, 0), (0, -1), (1, 0), (0, 1)}
        while q:
            i, j = q.popleft()
            for move in moves:
                if (i + move[0], j + move[1]) in ones and visited[i + move[0]][j + move[1]] != 1:
                    grp1[(i + move[0], j + move[1])] = 1
                    q.append((i + move[0], j + move[1]))
                    visited[i + move[0]][j + move[1]] = 1
        for p in ones:
            if p not in grp1:
                grp2[p] =  2
        

        visited = [[0]*len(grid[0]) for _ in range(len(grid))]
        q = deque()
        lev = 0
        for p in grp1:
            q.append(p)

        nxt = deque()
        while True:
            while q:
                i, j = q.popleft()
                for move in moves:
                    if (i + move[0], j + move[1]) in grp2: return lev
                    if 0 <= i + move[0] < len(grid) and  0 <= j + move[1] < len(grid[0]) and (i + move[0], j + move[1]) not in ones and visited[i + move[0]][j + move[1]] != 1:
                        nxt.append((i + move[0], j + move[1]))
                        visited[i + move[0]][j + move[1]] = 1
            if nxt != []:
                q = nxt.copy()
                lev += 1
                nxt = deque()
            else:
                return lev
        return lev