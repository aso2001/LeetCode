class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        visited = [False]*n
    
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        grp = []
        for i in range(n):
            cnt = 0
            if visited[i]:
                continue
            q = deque([i])
            while q:
                cur = q.popleft()
                cnt += 1
                visited[cur] = True
                for nei in adj[cur]:
                    if not visited[nei]:
                        visited[nei] = True
                        q.append(nei)
            grp.append(cnt)

        su = sum(grp)
        sq = sum(x*x for x in grp)
        return int((su*su - sq)/2)
        # res = 0
        # for i in range(len(grp)-1):
        #     for j in range(i+1, len(grp)):
        #         res += grp[i]*grp[j] 
        # return res