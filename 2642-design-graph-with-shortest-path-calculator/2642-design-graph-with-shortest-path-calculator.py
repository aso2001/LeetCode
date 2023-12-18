class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.dd = {}
        for a,b,c in edges:
            if a in self.dd:
                self.dd[a].append((b,c))
            else:
                self.dd[a] = [(b,c)]
        
    def addEdge(self, edge: List[int]) -> None:
        a, b, c = edge
        if a in self.dd:
            self.dd[a].append((b, c))
        else:
            self.dd[a] = [(b, c)]
        

    def shortestPath(self, node1: int, node2: int) -> int:
        import heapq
        g = [math.inf]*self.n
        g[node1] = 0

        q = [(0, node1)]
        heapq.heapify(q)
        while q:
            cst, cur = heapq.heappop(q)
            if cur not in self.dd:
                continue
            for nei in self.dd[cur]:
                if g[nei[0]] > cst + nei[1]:
                    g[nei[0]] = cst + nei[1]
                    heapq.heappush(q, (g[nei[0]], nei[0]))
        return g[node2] if g[node2] != math.inf else -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)