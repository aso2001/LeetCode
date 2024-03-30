class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.helper(nums, k) - self.helper(nums, k - 1)

    def helper(self, nums, distK):
        res, L, cnt = 0, 0, 0
        freq = Counter()
        for R in range(len(nums)):
            freq[nums[R]] += 1
            if freq[nums[R]] == 1:
                cnt += 1
            while cnt > distK:
                freq[nums[L]] -= 1
                if not freq[nums[L]]:
                    cnt -= 1
                L += 1
            res += R - L + 1
        return res