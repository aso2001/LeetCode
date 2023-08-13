class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = {}
        dp[-1] = True

        def rec(i):
            if i in dp:
                return dp[i]
            else:
                res = False
            if i > 0 and nums[i] == nums[i - 1]:
                res |= rec(i - 2)

            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                res |= rec(i - 3)
            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                res |= rec(i - 3)
            dp[i] = res
            return res

        return rec(len(nums) - 1)