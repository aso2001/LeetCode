class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        idx = list(range(len(bombs)))
        comb = combinations(idx, 2)
        for c in comb:
            a, b = c
            x1, y1, r1 = bombs[a]
            x2, y2, r2 = bombs[b]
            if (x1 - x2)**2 + (y1 - y2)**2 <= r1*r1:
                adj[a].append(b)
            if (x1 - x2)**2 + (y1 - y2)**2 <= r2*r2:
                adj[b].append(a)
        
        def bfs(s):
            q = deque()
            nxt = deque()
            q.append(s)
            visited = [0]*len(bombs)
            visited[s] = 1
            cnt = 1
            while True:
                while q:
                    cur = q.popleft()
                    for nei in adj[cur]:
                        if not visited[nei]:
                            visited[nei] = 1
                            nxt.append(nei)
                            cnt += 1
                if nxt:
                    q = nxt.copy()
                    nxt = deque()
                else:
                    return cnt
                
        res = 0
        for b in idx:
            res = max(res, bfs(b))
        return res        