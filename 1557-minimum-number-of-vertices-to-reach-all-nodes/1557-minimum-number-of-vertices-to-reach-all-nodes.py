class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        inc = defaultdict(list)
        for e in edges:
            if e[0] not in adj:
                adj[e[0]] = [e[1]]
            else:
                adj[e[0]].append(e[1])
            if e[1] not in inc:
                inc[e[1]] = [e[0]]
            else:
                inc[e[1]].append(e[0])   

        res = []
        for a in adj:
            if a not in inc:
                res.append(a)
        return res