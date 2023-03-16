class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        L, R = min(time), min(time)*totalTrips

        def trips(tottime):
            res = 0
            for t in time:
                res += tottime // t
            return res

        while L < R:
            mid = (L + R) // 2
            if trips(mid) < totalTrips:
                L = mid + 1
            else:
                R = mid
        return L