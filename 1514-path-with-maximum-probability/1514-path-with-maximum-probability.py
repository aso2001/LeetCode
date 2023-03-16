class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        visited = set()
        adj = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            adj[b].append((a, succProb[i])) 
            adj[a].append((b, succProb[i]))
            
        hh = []
        heapq.heappush(hh, [-1, start])

        while hh:
            prob, cur = heapq.heappop(hh)
            visited.add(cur)
            if cur == end:
                return -1 * prob
            for nei, nprob in adj[cur]:
                if nei not in visited:
                    heapq.heappush(hh, (prob * nprob, nei))         
        return 0