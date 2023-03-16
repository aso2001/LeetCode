class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        adj = defaultdict(list)
        for b, e in roads:
            adj[b].append(e)
            adj[e].append(b)
        
        def dfs(node, parent):
            nonlocal res
            reps = 0
            if node not in adj:
                return reps
            
            for nei in adj[node]:
                if nei != parent:
                    p = dfs(nei, node)
                    reps += p
                    res += math.ceil(p/seats)
            return reps + 1

        res = 0
        dfs(0, -1)
        return res