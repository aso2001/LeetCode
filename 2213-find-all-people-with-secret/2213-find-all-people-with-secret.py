class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        res = set([0, firstPerson])
        time = {}

        for m in meetings:
            if m[2] not in time:
                time[m[2]] = defaultdict(list)
            time[m[2]][m[0]].append(m[1])
            time[m[2]][m[1]].append(m[0])
        
        def dfs(src, adj):
            if src in visited:
                return
            visited.add(src)
            res.add(src)
            for nei in adj[src]:
                dfs(nei, adj)
        
        for t in sorted(time.keys()):
            visited = set()
            for src in time[t]:
                if src in res:
                    dfs(src, time[t])

        return list(res)