class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inc = defaultdict(list)
        for src, dist in edges:
            inc[dist].append(src)   

        res = []
        for a in range(n):
            if a not in inc:
                res.append(a)
        return res