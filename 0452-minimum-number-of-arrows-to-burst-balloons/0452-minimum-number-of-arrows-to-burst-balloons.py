class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = len(points)
        prev = points[0]
        for i in range(1, len(points)):
            if points[i][0] > prev[1]:
                prev = points[i]
            else:
                res -= 1
                prev[0] = points[i][0]
                prev[1] = min(points[i][1], prev[1])
        return res