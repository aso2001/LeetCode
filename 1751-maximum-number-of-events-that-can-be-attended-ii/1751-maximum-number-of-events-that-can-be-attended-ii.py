class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key = lambda x: x[1])
        def helper(i, prev, k, d):
            if not k or i >= len(events):
                return 0
            elif (i, prev, k) in d:
                return d[(i, prev, k)]
            elif events[i][0] > prev:
                j = i
                endDay = events[i][1]
                while j < len(events) and events[j][0] <= endDay:
                    j += 1
                d[(i, prev, k)] = max(events[i][2] + helper(j, endDay, k - 1, d), helper(i + 1, prev, k, d))
                return d[(i, prev, k)]
            else:
                d[(i, prev, k)] = helper(i + 1, prev, k, d)
                return d[(i, prev, k)]
        d = {}
        return helper(0, 0, k, d)