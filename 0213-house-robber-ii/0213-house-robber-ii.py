class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]
        if len(nums) <= 3: return max(nums)
        max1 = 0
        max2 = nums[0]
        for i in range(1, len(nums) - 1):
            tsum = max(max1 + nums[i], max2)
            max1 = max2
            max2 = tsum
        tt1 = tsum
        max1 = 0
        max2 = nums[1]
        for i in range(2, len(nums)):
            tsum = max(max1 + nums[i], max2)
            max1 = max2
            max2 = tsum
        tt2 = tsum
        return max(tt1, tt2)