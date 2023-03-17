class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2: return max(nums)

        max1 = nums[0]
        max2 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            tsum = max(max1 + nums[i], max2)
            max1 = max2
            max2 = tsum
        return tsum

    #     P(0) = M(0)
    #     P(1) = M(1)
    #     P(k) = Max(P(k-2) + M(k), P(k-1))