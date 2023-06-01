class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]: return -1
        n = len(grid)
        if n == 1: return 1
        visited = [[0]*n for _ in range(n)]
        visited[0][0] = 1

        moves = {(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)}

        cost = 1
        q = deque([[0,0]])
        nxt = deque()
        while True:
            while q:
                cur = q.popleft()
                for mv in moves:
                    if 0 <= cur[0] + mv[0] < n and 0 <= cur[1] + mv[1] < n and grid[cur[0] + mv[0]][cur[1] + mv[1]] == 0:
                        if cur[0] + mv[0] == n - 1 and cur[1] + mv[1] == n -1:
                            return cost + 1
                        if visited[cur[0] + mv[0]][cur[1] + mv[1]] != 1:
                            nxt.append((cur[0] + mv[0], cur[1] + mv[1]))
                            visited[cur[0] + mv[0]][cur[1] + mv[1]] = 1
            if nxt:
                q = nxt.copy()
                nxt = deque()
                cost += 1
            else:
                return -1 