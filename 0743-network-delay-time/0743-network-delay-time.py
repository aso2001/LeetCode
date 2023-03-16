class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

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