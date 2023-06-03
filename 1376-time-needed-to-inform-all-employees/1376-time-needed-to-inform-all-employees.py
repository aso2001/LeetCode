class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] == -1: continue
            if manager[i] in adj:
                adj[manager[i]].append(i)
            else:
                adj[manager[i]] = [i]

        def dfs(i):
            if i not in adj:
                return 0
            res = 0
            for nei in adj[i]:
                res = max(res, informTime[nei] + dfs(nei))
            return res

        return informTime[headID] + dfs(headID)