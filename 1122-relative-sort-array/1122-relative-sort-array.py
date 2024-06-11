class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a2 =set(arr2)
        xtra = []
        dd = defaultdict(int)
        for a in arr1:
            if a in a2:
                dd[a] += 1
            else:
                xtra.append(a)
        xtra.sort()
        res = []
        for a in arr2:
            res.extend([a]*dd[a])
        res = res + xtra
        return res