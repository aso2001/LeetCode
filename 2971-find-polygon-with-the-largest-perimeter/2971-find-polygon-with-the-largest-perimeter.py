class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        px = nums[0]
        for i in range(2, len(nums)):
            px += nums[i - 1]
            if px > nums[i]:
                res = px + nums[i]
        return res