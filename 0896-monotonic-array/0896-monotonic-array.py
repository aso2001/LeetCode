class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                if i == len(nums) - 1:
                    return True
                continue
            else:
                break
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                if i == len(nums) - 1:
                    return True
                continue
            else:
                return False      