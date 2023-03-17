class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 2
        dp = len(nums) - 1
        while i >= 0 and dp != 0:
            if nums[i] >= dp - i:
                dp = i
            i -= 1
            if i < 0 and dp != 0:
                return False
        if dp == 0: return True