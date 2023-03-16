class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k):
            res = 0
            for p in piles:
                res += math.ceil(p/k)
            return res

        L, R = 1, sum(piles)

        while L <= R:
            mid = (L + R) // 2
            hmid = helper(mid)
            if hmid > h:
                L = mid + 1
            elif hmid < h:
                R = mid - 1
            else:
                break

        while helper(mid) == h:
            mid -= 1
        if helper(mid) > h:
            return mid + 1
        else:
            return mid


    def minEatingSpeed2(self, piles: List[int], h: int) -> int:
        def hours(k):
            hh = 0
            for p in piles:
                hh += math.ceil(p/k)
            return hh

        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l + r)//2
            if hours(mid) > h:
                l = mid + 1
            elif hours(mid) <= h:
                res = min(res, mid)
                r = mid - 1
        return res