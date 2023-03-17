class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r - 1: # len(nums) > 2
            mid = (l + r)//2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid 
            if nums[mid] > nums[mid + 1]:
                r = mid - 1
            else:
                l = mid + 1
        # len(nums) <= 2
        return l if nums[l] > nums[r] else r