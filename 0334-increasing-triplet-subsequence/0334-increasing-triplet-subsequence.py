class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        min1 = min2 = math.inf
        for i in range(len(nums)):
            if nums[i] < min1:
                min1 = nums[i]
            elif nums[i] > min1 and nums[i] < min2:
                min2 = nums[i]
            elif nums[i] > min2:
                return True
        return False