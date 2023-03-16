class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def time(capacity):
            i, cnt = 0, 0
            while i < len(weights):
                ss = 0
                while i < len(weights) and ss + weights[i] <= capacity:
                    ss += weights[i]
                    i += 1
                cnt += 1
            return cnt

        L, R = max(weights), sum(weights)
        while L <= R:
            mid = (L + R) // 2
            tt = time(mid)
            if tt <= days:
                R = mid - 1
            elif tt > days:
                L = mid + 1
        return L