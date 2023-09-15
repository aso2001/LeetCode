class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        res = 0
        visited = set()
        minH = [[0,0]]

        adj = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        while len(visited) < len(points):
            cost, v = heapq.heappop(minH)
            if v in visited:
                continue
            res += cost
            visited.add(v)
            for nei in adj[v]:
                heapq.heappush(minH, nei)
        return res