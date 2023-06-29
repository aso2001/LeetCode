class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        visited = defaultdict(set)
        
        key_set, lock_set = set(), set()
        all_keys = 0
        start_r, start_c = -1, -1
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell in 'abcdef':
                    all_keys += (1 << (ord(cell) - ord('a')))
                    key_set.add(cell)
                if cell in 'ABCDEF':
                    lock_set.add(cell)
                if cell == "@":
                    start_r, start_c = i, j
        
        q.append((start_r, start_c, 0, 0))
        visited[0].add((start_r, start_c))
        moves = ((0, 1), (1, 0), (-1, 0), (0, -1))
        while q:
            cur_r, cur_c, keys, dist = q.popleft()
            for dr, dc in moves:
                new_r, new_c = cur_r + dr, cur_c + dc
                if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] != '#':
                    cell = grid[new_r][new_c]
                    if cell in key_set and not ((1 << (ord(cell) - ord('a'))) & keys):
                        new_keys = (keys | (1 << (ord(cell) - ord('a'))))
                        if new_keys == all_keys:
                            return dist + 1
                        visited[new_keys].add((new_r, new_c))
                        q.append((new_r, new_c, new_keys, dist + 1))
                    elif cell in lock_set and not (keys & (1 << (ord(cell) - ord('A')))):
                        continue
                    elif (new_r, new_c) not in visited[keys]:
                        visited[keys].add((new_r, new_c))
                        q.append((new_r, new_c, keys, dist + 1))     
        return -1