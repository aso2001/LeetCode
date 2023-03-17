class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Bottom-up approach. Solve all subproblems first of length 1,2,..
        nums = [1] + nums + [1]
        dp = [[0]*len(nums) for _ in range(len(nums))]
        
        for offset in range(1, len(nums) - 1):
            for L in range(0, len(nums) - 1 - offset):
                R = L + offset + 1
                for i in range(L + 1, R):
                    dp[L][R] = max(dp[L][R], nums[L]*nums[i]*nums[R] + dp[L][i] + dp[i][R])
        return dp[0][len(nums)-1]

    
    def maxCoins2(self, nums: List[int]) -> int:
        # Top-down approach with memorization and optimization  
        nums = [1] + nums + [1]
        dp = [[-math.inf]*len(nums) for _ in range(len(nums))]

        @cache
        def dfs(L, R):
            if L > R:
                return 0
            if dp[L][R] >= 0:
                return dp[L][R]

            dp[L][R] = 0
            for i in range(L, R + 1):
                dp[L][R] = max(dp[L][R], nums[L - 1] * nums[i] * nums[R + 1] + dfs(i + 1, R) + dfs(L, i - 1))
            return dp[L][R] 

        return dfs(1, len(nums) - 2)

        # 718 = 56 => 31578
        # 578 = 280 => 3158
        # 315 = 15 => 358
        # 358 = 120 => 38
        # 138 = 24 => 8
        # 8


