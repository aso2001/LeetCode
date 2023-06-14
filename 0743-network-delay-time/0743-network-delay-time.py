class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {i:[] for i in range(1, n+1)}
        res = [math.inf]*n
        for u, v, w in times:
            adj[u].append([v, w])

        res[k-1] = 0
        visited = [False]*n
        hh = [[0, k]]
        while hh:
            cur = heapq.heappop(hh)
            if visited[cur[1] - 1]:
                continue
            visited[cur[1] - 1] = True
            for nei in adj[cur[1]]:
                if not visited[nei[0] - 1]:
                    if cur[0] + nei[1] < res[nei[0] - 1]:
                        res[nei[0] - 1] = cur[0] + nei[1]
                    heapq.heappush(hh, [res[nei[0] - 1], nei[0]])
        return -1 if max(res) == math.inf else max(res)
    
    
    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {i:[] for i in range(n)}

        for t in times:
            adj[t[0] - 1].append([t[1], t[2]])

        g = [math.inf]*n
        g[k - 1] = 0
        visited = set()

        minH = [[0, k]]
        while minH:
            dist, v = heapq.heappop(minH)
            if v in visited:
                continue
            visited.add(v)
            for nei in adj[v - 1]:
                if nei[0] not in visited:
                    if g[nei[0] - 1] > dist + nei[1]:
                        g[nei[0] - 1] = dist + nei[1]
                    pair = [g[nei[0] - 1], nei[0]]
                    heapq.heappush(minH, pair)

        return -1 if max(g) == math.inf else max(g)