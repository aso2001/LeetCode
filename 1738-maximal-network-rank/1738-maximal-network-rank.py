class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for b, e in roads:
            if b in adj:
                adj[b].append(e)
            else:
                adj[b] = [e]
            if e in adj:
                adj[e].append(b)
            else:
                adj[e] = [b]
        
        res = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    res = max(res, (len(adj[i]) + len(adj[j]) - (1 if j in adj[i] else 0)))
        return res