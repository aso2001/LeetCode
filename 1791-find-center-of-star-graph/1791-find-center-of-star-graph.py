class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dd = defaultdict(int)
        for e in edges:
            dd[e[0]] += 1
            dd[e[1]] += 1
        for d in dd:
            if dd[d] > 1:
                return d