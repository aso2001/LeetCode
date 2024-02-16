class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dd = defaultdict(int)
        for a in arr:
            dd[a] += 1
        dd = dict(sorted(dd.items(), key=lambda x:x[1]))
        for d in dd:
            if dd[d] <= k:
                k -= dd[d]
                dd[d] = 0
            if not k:
                break
        res = 0
        for d in dd:
            if dd[d] > 0:
                res += 1
        return res