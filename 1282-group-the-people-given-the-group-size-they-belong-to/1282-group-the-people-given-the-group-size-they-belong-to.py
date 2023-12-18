class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dd = defaultdict(list) 
        for i in range(len(groupSizes)):
            dd[groupSizes[i]].append(i)
        res = []
        for grp, arr in dd.items():
            l1 = []
            for k in range(len(arr)):
                if len(l1) == grp:
                    res.append(l1)
                    l1 = []
                l1.append(arr[k])
            res.append(l1)
        return res