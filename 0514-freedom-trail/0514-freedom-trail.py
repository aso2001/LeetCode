class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = {}

        def rec(r, k):
            if k == len(key):
                return 0
            if (r, k) in dp:
                return dp[(r, k)]
            res = math.inf
            for i in range(len(ring)):
                if ring[i] == key[k]:
                    min_dist = min(abs(r - i), len(ring) - abs(r - i))
                    res = min(res, min_dist + 1 + rec(i, k + 1))
            dp[(r, k)] = res
            return res

        return rec(0, 0)