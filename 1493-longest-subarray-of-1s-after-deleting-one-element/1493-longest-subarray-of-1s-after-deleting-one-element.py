class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, L, L1, cnt = 0, 0, 0, 0
        for R in range(len(nums)):
            if not nums[R]:
                if not cnt:
                    L1 = R + 1
                    cnt = 1
                else:
                    res = max(res, R - L - 1)
                    L = L1
                    L1 = R + 1
        return max(res, R - L)