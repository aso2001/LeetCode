class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dd = defaultdict(int)
        for n in nums:
            dd[n] += 1
        dmax = max(dd.values())
        res = 0
        for d in dd.keys():
            if dd[d] == dmax:
                res += dmax
        return res