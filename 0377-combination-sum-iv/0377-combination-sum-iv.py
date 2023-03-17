class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Top-down DP
        dp = {}

        def dfs(target):
            if target in dp:
                return dp[target]
            if target == 0:
                return 1
            if target < 0:
                return 0
            dp[target] = 0
            for n in nums:
                dp[target] += dfs(target - n)
            return dp[target]
        return dfs(target)
    
    
    def combinationSum4_2(self, nums: List[int], target: int) -> int:
        # Bottom up approach
        dp = [0]*(target + 1)
        dp[0] = 1
        for index in range(len(dp)):
            for num in nums:
                if num <= index:
                    dp[index] += dp[index - num]
        return dp[target]