class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dd = {}
        for a in arr:
            if a in dd:
                dd[a] += 1
            else:
                dd[a] = 1
        res = set()
        for a in dd:
            res.add(dd[a])
        return len(res) == len(dd)