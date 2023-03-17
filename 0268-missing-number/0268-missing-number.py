class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int((len(nums) + 1)/2*len(nums)) - sum(nums)