class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        res = 0
        visited = [False]*n
        visited[0] = True

        edges = {(a, b) for a,b in connections}

        d = defaultdict(list)
        for a, b in connections:
            d[b].append(a)
            d[a].append(b)
            
        def dfs(i):
            nonlocal res
            for nei in d[i]:
                if not visited[nei]:
                    visited[nei] = True
                    if (nei, i) not in edges:
                        res += 1
                    dfs(nei)
                    
        dfs(0)
        return res