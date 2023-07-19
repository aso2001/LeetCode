class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0]
        cnt = 0
        for ii in intervals[1:]:
            if prev[1] <= ii[0]:
                prev = ii
            elif prev[0] <= ii[0] and prev[1] >= ii[1]:
                prev = ii
                cnt += 1
            elif prev[0] <= ii[0] and prev[1] <= ii[1]:
                cnt += 1
        return cnt