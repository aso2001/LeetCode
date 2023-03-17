class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tickets.sort()
        adj = {}
        for (fr, to) in tickets:
            if fr not in adj: adj[fr] = [to]
            else: adj[fr].append(to)

        res = ['JFK']
        def dfs(fr):
            if len(res) == len(tickets) + 1:
                return True

            if fr not in adj:
                return False

            tmp = adj[fr].copy()
            for to in tmp:
                res.append(to)
                adj[fr].pop(0)
                if dfs(to): 
                    return True
                else:
                    res.pop()
                    adj[fr].append(to)

        dfs('JFK')
        return res