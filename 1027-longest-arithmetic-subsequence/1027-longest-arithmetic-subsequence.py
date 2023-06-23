class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        
        for R in range(len(nums)):
            for L in range(R):
                dp[(R, nums[R] - nums[L])] = dp.get((L, nums[R] - nums[L]), 1) + 1   
        
        return max(dp.values())