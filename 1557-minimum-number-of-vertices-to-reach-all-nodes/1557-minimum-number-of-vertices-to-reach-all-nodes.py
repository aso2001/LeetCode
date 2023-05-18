class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inc = defaultdict(list)
        for src, dist in edges:
            if dist not in inc:
                inc[dist] = [src]
            else:
                inc[dist].append(src)   

        res = []
        for a in range(n):
            if a not in inc:
                res.append(a)
        return res