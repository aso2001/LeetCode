class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        def dfs(nums):
            if len(nums) < 3:
                return 1
            left = [a for a in nums if a < nums[0]]
            right = [a for a in nums if a > nums[0]]
            return dfs(left)*dfs(right)*comb(len(nums) - 1, len(left)) % mod

        return (dfs(nums) - 1) % mod    