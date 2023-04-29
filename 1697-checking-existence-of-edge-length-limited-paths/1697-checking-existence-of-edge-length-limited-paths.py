class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dd = defaultdict()

        def find(x):
            if x not in dd:
                return x
            else:
                if x != dd[x]:
                    dd[x] = find(dd[x])
                return dd[x]

        def union(x,y):
            a = find(x)
            b = find(y)
            if a != b:
                dd[b] = a

        edgeList.sort(key = lambda x: x[2])
        
        res = [False]*len(queries)
        
        i = 0
        for limit, x, y, idx in sorted((q[2], q[0], q[1], i) for i, q in enumerate(queries)):
            while i < len(edgeList) and edgeList[i][2] < limit:
                union(edgeList[i][0], edgeList[i][1])
                i += 1
            res[idx] = find(x) == find(y)
            
        return res