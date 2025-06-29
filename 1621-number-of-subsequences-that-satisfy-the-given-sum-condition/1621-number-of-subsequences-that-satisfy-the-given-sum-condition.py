class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = 0
        L = 0 
        R = len(nums) - 1
        mod = 10**9 + 7

        while L <= R:
            if nums[L] + nums[R] <= target:
                res = (res + (2**(R - L)) % mod) % mod
                L += 1
            else:
                R -= 1
        return res