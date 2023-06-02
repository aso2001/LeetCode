class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(bombs)-1):
            for j in range(i+1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                if (x1 - x2)**2 + (y1 - y2)**2 <= r1*r1:
                    adj[i].append(j)
                if (x1 - x2)**2 + (y1 - y2)**2 <= r2*r2:
                    adj[j].append(i)
            
        def dfs(s):
            q = deque()
            q.append(s)
            visited = [0]*len(bombs)
            visited[s] = 1
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if not visited[nei]:
                        visited[nei] = 1
                        q.append(nei)
            return sum(visited)
                
        res = 0
        for b in range(len(bombs)):
            res = max(res, dfs(b))
        return res      