class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dd = {}
        for a in adjacentPairs:
            if a[0] in dd:
                dd[a[0]].append(a[1])
            else:
                dd[a[0]] = [a[1]]
            if a[1] in dd:
                dd[a[1]].append(a[0])
            else:
                dd[a[1]] = [a[0]]
        
        for start in dd:
            if len(dd[start]) == 1:
                break
        
        res = [start, dd[start][0]]
        prev = start
        del dd[start]
        while dd:
            if len(dd[res[-1]]) == 1:
                return res
            if dd[res[-1]][0] == prev:
                nxt = dd[res[-1]][1]
            else:
                nxt = dd[res[-1]][0]
            prev = res[-1]
            res.append(nxt)
            del dd[prev]