class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for i in range(len(graph)):
            adj[i] = graph[i]
        red = set()
        green = set()
        tot = [i for i in range(len(graph))]
        q = [0]
        nxt = []
        col = 0
        while True:
            while q:
                cur = q.pop()
                if cur in tot:
                    tot.remove(cur)
                if col == 0:
                    if cur in green:
                        return False
                    elif cur not in red:
                        red.add(cur)
                    for nei in adj[cur]:
                        if nei in red:
                            return False
                        elif nei not in green:
                            nxt.append(nei)
                elif col == 1:
                    if cur in red:
                        return False
                    elif cur not in green:
                        green.add(cur)
                    for nei in adj[cur]:
                        if nei in green:
                            return False
                        elif nei not in red:
                            nxt.append(nei)
            print(cur, nxt)
            if not nxt:
                if not tot:
                    print(list(red))
                    print(list(green))
                    return True
                else:
                    q = [tot.pop()]
            else:
                q = nxt.copy()
            nxt = []
            col = 0 if col else 1