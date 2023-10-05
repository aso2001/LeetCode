class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dd = defaultdict(int)
        res = []
        for n in nums:
            dd[n] += 1
        for d in dd.keys():
            if dd[d] > len(nums)/3:
                res.append(d)
        return res