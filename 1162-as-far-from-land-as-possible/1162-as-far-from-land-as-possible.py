class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        visited = [[False]*len(grid) for _ in range(len(grid))]

        q = deque()

        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    q.append((i, j))

        if not q or len(q) == len(grid)*len(grid):
            return -1
        nxt, cnt = deque(), 0
        while True:
            while q:
                i, j = q.popleft()
                visited[i][j] = True
                for di, dj in moves:
                    if i + di < 0 or i + di == len(grid) or j + dj < 0 or j + dj == len(grid) or visited[i + di][j + dj]:
                        continue
                    visited[i + di][j + dj] = True
                    nxt.append((i + di, j + dj))
            if not nxt:
                return cnt
            q = nxt.copy()
            nxt = deque()
            cnt += 1