class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sat = satisfaction
        sat.sort()

        res = 0
        for i in range(len(sat) - 1, -1, -1):
            ss = 0
            for j in range(len(sat) - 1, i - 1, -1):
                ss += sat[j]*(j - i + 1)
            res = max(res, ss)
        return res

    #    -8 -14 -3  0 25
    #     0 -7  -2  0 20
    #     0  0  -1  0 15
    #     0  0  0   0 10
    #     0  0  0   0 5
    #    -8 -7  -1  0 5 