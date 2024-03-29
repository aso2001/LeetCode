class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_n = max(nums)
        res, L, max_cnt = 0, 0, 0

        for R in range(len(nums)):
            if nums[R] == max_n:
                max_cnt += 1
            while max_cnt == k:
                if nums[L] == max_n:
                    max_cnt -= 1
                L += 1
            res += L
        return res