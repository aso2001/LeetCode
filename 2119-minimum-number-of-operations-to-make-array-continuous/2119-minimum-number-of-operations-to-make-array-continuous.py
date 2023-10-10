class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n =  len(nums)
        nums = sorted(set(nums))

        i = 0
        for item in nums:
            i += item - nums[i] > n - 1
        return i + n - len(nums)