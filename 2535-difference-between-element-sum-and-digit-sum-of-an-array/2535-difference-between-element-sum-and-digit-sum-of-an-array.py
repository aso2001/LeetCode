class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        nsum = sum(nums)
        dsum = 0
        for i in range(len(nums)):
            tmp = nums[i]
            while tmp:
                dsum += tmp%10
                tmp //= 10
        return abs(nsum - dsum)   