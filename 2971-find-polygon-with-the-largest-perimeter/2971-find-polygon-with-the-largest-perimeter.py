class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res = -1
        px = 0
        for n in nums:
            if px > n:
                res = px + n
            px += n
        return res