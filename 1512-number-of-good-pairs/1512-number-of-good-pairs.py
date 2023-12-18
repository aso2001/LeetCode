class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dd = defaultdict(int)
        for n in nums:
            dd[n] += 1
        res = 0
        for d in dd.values():
            res += math.comb(d, 2)
        return res