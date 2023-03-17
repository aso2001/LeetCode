class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ii = intervals
        ii.sort()
        li = len(ii)

        if li == 1: return ii

        res = []
        prev = ii[0]
        for i in range(1, li):
            if ii[i][0] <= prev[1]:
                prev = [prev[0], ii[i][1]] if ii[i][1] > prev[1] else [prev[0], prev[1]]
            else:
                res.append(prev)
                prev = ii[i]
            if i == li - 1: res.append(prev)
        return res
            