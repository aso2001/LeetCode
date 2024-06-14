class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        prev = nums[0]
        res = 0
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                res += prev - nums[i] + 1
                nums[i] += prev - nums[i] + 1
            prev = nums[i]
        return res