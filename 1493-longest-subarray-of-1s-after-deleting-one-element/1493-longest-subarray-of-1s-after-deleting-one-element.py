class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt0, cnt1 = 0, 0
        for n in nums:
            if n:
                cnt1 += 1
            else:
                cnt0 += 1
        if cnt0 == len(nums): return 0
        elif cnt1 == len(nums): return len(nums) - 1

        L = 0
        L1 = L
        mx = 0
        cnt0 = 0
        for R in range(len(nums)):
            if nums[R] == 0 and cnt0 == 0:
                L1 = R + 1
                cnt0 = 1
            elif nums[R] == 0 and cnt0 == 1:
                mx = max(mx, R - L - 1)
                L = L1
                L1 = R + 1
        if R == len(nums) - 1:
            mx = max(mx, R - L)
        return mx