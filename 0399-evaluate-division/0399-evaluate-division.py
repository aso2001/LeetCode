class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])

        def bfs(a, b):
            if a not in adj or b not in adj:
                return -1
            q = deque()
            q.append([a, 1])
            visited = set()
            while q:
                cur, cv = q.popleft()
                if cur == b:
                    return cv
                visited.add(cur)
                for nei, v in adj[cur]:
                    if nei not in visited:
                        q.append([nei, cv*v])
            return -1
        
        res = []
        for a, b in queries:
            res.append(bfs(a, b))
        return res