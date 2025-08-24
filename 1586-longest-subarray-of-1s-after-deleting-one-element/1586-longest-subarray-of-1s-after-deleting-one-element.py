class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, L, cnt = 0, 0, 0
        for R in range(len(nums)):
            if not nums[R]:
                cnt += 1
            while cnt > 1:
                if not nums[L]:
                    cnt -= 1
                L += 1
            res = max(res, R - L)
        return res

    def longestSubarray2(self, nums: List[int]) -> int:
        res, L, L1, cnt = 0, 0, 0, 0
        for R in range(len(nums)):
            if not nums[R]:
                if not cnt:
                    cnt = 1
                else:
                    res = max(res, R - L - 1)
                    L = L1
                L1 = R + 1
        return max(res, R - L)
        
        # 0 1 1 1 0 1 1 0 1