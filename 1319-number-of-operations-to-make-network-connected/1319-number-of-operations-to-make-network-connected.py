class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) + 1 < n:
            return -1

        visited = [False]*n
        vtx = [i for i in range(n)]

        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)

        q = deque()
        q.append(0)

        cnt = 0
        while True:
            while q:
                cur = q.popleft()
                visited[cur] = True
                if cur in vtx:
                    vtx.remove(cur)
                for nei in adj[cur]:
                    if not visited[nei]:
                        q.append(nei)
                        visited[nei] = True
            if not vtx:
                break
            q.append(vtx.pop(0))
            cnt += 1
        return cnt