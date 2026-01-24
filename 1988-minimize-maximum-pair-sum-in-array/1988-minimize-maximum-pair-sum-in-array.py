class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = -math.inf
        for i in range(len(nums)//2+1):
            res = max(res, nums[i] + nums[len(nums) - i - 1])
        return res