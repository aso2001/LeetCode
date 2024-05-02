class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        L, R = 0, len(nums) - 1
        while L < R:
            if nums[L] < 0 and nums[R] > 0:
                if abs(nums[L]) > nums[R]:
                    L += 1
                elif abs(nums[L]) < nums[R]:
                    R -= 1
                else:
                    return nums[R]
            else:
                return -1
        return -1