class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # O(1) extra space complexity solution
        res = [1]*len(nums)
        p, s = 1, 1

        for i in range(len(nums) - 1):
            p *= nums[i]
            res[i + 1] = p
        for i in range(len(nums) - 1, 0, -1):
            s *= nums[i]
            res[i - 1] = s * res[i - 1]
        return res