class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if len(nums) == 1: return 1
        nums.sort()
        i, s, res = 0, 0, 0
        for j in range(1, len(nums)):
            s += (nums[j] - nums[j - 1])*(j - i)
            while s > k and i < j:
                s -= nums[j] - nums[i]
                i += 1
            res = max(res, j - i + 1)
        return res