class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        n = len(garbage)
        m, p, g = n - 2, n - 2, n - 2
        for i in range(n - 1, -1, -1):
            if 'M' not in garbage[i] and m == i - 1:
                m -= 1
            if 'P' not in garbage[i] and p == i - 1:
                p -= 1
            if 'G' not in garbage[i] and g == i - 1:
                g -= 1
        res += (sum(travel[:m+1]) if m >= 0 else 0) + (sum(travel[:p+1]) if p >= 0 else 0) + (sum(travel[:g+1]) if g >= 0 else 0)
        for g in garbage:
            res += len(g)
        return res