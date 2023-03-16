class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res, tmp = [], 0
        for i in range(len(nums)):
            tmp += nums[i]
            res.append(tmp)
        return res