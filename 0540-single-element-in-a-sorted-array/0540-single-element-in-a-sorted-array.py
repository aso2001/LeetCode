class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        L, R = 0, len(nums) - 1
        while L <= R:
            mid = L + ((R - L) // 2)
            if (mid < 1 or nums[mid - 1] != nums[mid]) and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1]):
                return nums[mid]
            leftSide = mid - 1 if nums[mid - 1] == nums[mid] else mid
            if leftSide%2:
                R = mid - 1
            else:
                L = mid + 1