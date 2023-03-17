class Solution:
    def integerBreak(self, n: int) -> int:
        # DP solution
        dp = {1:1}

        for num in range(2, n + 1):
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dp[i] * dp[num - i]
                dp[num] = max(val, dp[num])
        return dp[n]
    

    def integerBreak1(self, n: int) -> int:
        # Recursive
        dp = {1:1}

        def dfs(num):
            if num in dp:
                return dp[num]
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                dp[num] = max(val, dp[num])
            return dp[num]

        return dfs(n)
    

    def integerBreak2(self, n: int) -> int:
        # Math solution
        if n == 2 or n == 3: return n - 1
        res = 1
        while n > 4:
            n -= 3
            res *= 3
        return res*n

        # 7: 3*4=12
        # 8: 4*4=16 3*3*2=18
        # 9: 4*5=20 3*3*3=27 2*2*2*3
        # 10: 5*5=10 3*3*4=36