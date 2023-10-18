class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        @cache
        def dfs(node):
            if not graph[node]:
                return time[node]  
            res = 0
            for nei in graph[node]:
                res = max(res, dfs(nei))
            return time[node] + res
            
        graph = defaultdict(list)
        for (x, y) in relations:
            graph[x - 1].append(y - 1)
        res = 0
        for node in range(n):
            res = max(res, dfs(node))
        return res        