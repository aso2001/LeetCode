class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)

        def dfs(i):
            if i in path:
                return float(inf)
            if i in visited:
                return 0

            visited.add(i)
            path.add(i)
            idx = ord(colors[i]) - ord('a')
            s[i][idx] = 1
            for nei in adj[i]:
                if dfs(nei) == float(inf):
                    return float(inf)
                for c in range(26):
                    s[i][c] = max(s[nei][c] + (1 if c == idx else 0), s[i][c])
            path.remove(i)
            return max(s[i])
    
        res = 0
        visited, path = set(), set()
        s = [[0]*26 for _ in range(len(colors))]
        for i in range(len(colors)):
            res = max(res, dfs(i))
        return -1 if res == float(inf) else res