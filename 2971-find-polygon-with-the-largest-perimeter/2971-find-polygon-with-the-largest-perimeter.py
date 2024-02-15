class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        px = [0]*len(nums)
        ss = 0
        for i in range(len(nums)):
            ss += nums[i]
            px[i] = ss
        res = -1
        ix = -1
        for i in range(2, len(nums)):
            if px[i - 1] > nums[i]:
                res = px[i]
                ix = i
        return res