class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        L, R = 0, len(nums) - 1
        while L <= R:
            if nums[L] < nums[R]:
                return nums[L]
            mid = (L + R)//2
            if nums[mid] > nums[mid + 1]:
                 return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if  nums[L] < nums[mid]:
                L = mid + 1
            else:
                R = mid - 1