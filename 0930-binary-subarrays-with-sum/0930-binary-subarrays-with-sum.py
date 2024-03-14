class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def helper(x):
            if x < 0: return 0
            
            res = 0
            L, cur = 0, 0
            for R in range(len(nums)):
                cur += nums[R]
                while cur > x:
                    cur -= nums[L]
                    L += 1
                res += (R - L + 1)
            return res
        
        return helper(goal) - helper(goal - 1)