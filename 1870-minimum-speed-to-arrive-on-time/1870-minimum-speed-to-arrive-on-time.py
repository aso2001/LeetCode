class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) >= hour + 1: return -1

        L, R = 1, ceil(max(max(dist),dist[-1]/(1 if hour.is_integer() else hour-int(hour))))

        while L < R:
            mid = (L + R) // 2
            ss = 0
            for d in dist[:-1]:
                ss += ceil(d/mid)
            ss += dist[-1]/mid
            if ss <= hour:
                R = mid
            else:
                L = mid + 1
        return L