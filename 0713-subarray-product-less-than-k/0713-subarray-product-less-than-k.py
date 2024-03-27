class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        res = 0
        prod = 1
        L = 0
        for R, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod //= nums[L]
                L += 1
            res += R - L + 1
        return res