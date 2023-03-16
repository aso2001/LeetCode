class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        s_max = -math.inf
        s_min = math.inf
        s_tot = 0
        res_max = -math.inf
        res_min = math.inf

        for i in range(len(nums)):
            s_tot += nums[i]

            s_max = max(s_max + nums[i], nums[i])   #  [--][++++][--] = regular Kadane's Algo
            res_max = max(res_max, s_max)

            s_min = min(s_min + nums[i], nums[i])   #  [+++][--][++]  = s_tot - s_min
            res_min = min(res_min, s_min)
        
        if res_min == s_tot: res_min = math.inf #if all nums are negative
        return max(res_max, s_tot - res_min)