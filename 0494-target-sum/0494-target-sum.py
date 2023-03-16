class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # DP solution
        tot = sum(nums)
        dp = [[0]*(2*tot + 1) for _ in range(len(nums) + 1)]
        dp[0][nums[0] + tot] = 1
        dp[0][-nums[0] + tot] += 1
        
        for i in range(len(nums)):
            for ss in range(-tot, tot + 1):
                if dp[i - 1][ss + tot] > 0:
                    dp[i][ss + nums[i] + tot] += dp[i - 1][ss + tot]
                    dp[i][ss - nums[i] + tot] += dp[i - 1][ss + tot]

        return 0 if abs(target) > tot else dp[len(nums) - 1][target + tot]
    
    
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        # DP solution O(n*tot_sum). Recursion with memorization.

        dp = {}

        def backtrack(i, t):
            if i == len(nums):
                if t == target:
                    return 1
                return 0
            if (i, t) in dp:
                return dp[(i, t)]
            dp[(i, t)] = (backtrack(i + 1, t + nums[i]) + backtrack(i + 1, t - nums[i]))
            return dp[(i, t)]

        return backtrack(0, 0)

    
    def findTargetSumWays3(self, nums: List[int], target: int) -> int:
        # Brute-force recursion O(2^n). TLE

        def backtrack(i, t):
            nonlocal cnt
            if i == len(nums) - 1:
                if t == target:
                    cnt += 1
                return
            backtrack(i + 1, t + nums[i + 1])
            backtrack(i + 1, t - nums[i + 1])
        
        cnt = 0
        backtrack(-1, 0)
        return cnt