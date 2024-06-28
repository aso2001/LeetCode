class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        dd = defaultdict(int)
        for a,b in roads:
            dd[a] += 1
            dd[b] += 1
        cc = []
        for d in dd:
            cc.append((dd[d]))
        cc.sort(reverse=True)
        res = 0
        for c in cc:
            res += n*c
            n -= 1
        return res