class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res, L = 0, -1
        freq = Counter()
        for R in range(len(nums)):
            freq[nums[R]] += 1
            while freq[nums[R]] > k:
                L += 1
                freq[nums[L]] -= 1
            res = max(res, R - L)
        return res