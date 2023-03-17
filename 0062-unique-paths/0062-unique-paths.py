# Brute-force Recursive solution (LRU cache)
# Exponential time, exponential space
class Solution:
    @lru_cache(maxsize=1024)
    def uniquePaths1(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    
# Recursive solution with Memoization
# O(m*n) time, O(m*n) space, but limited by max call stack to overflow
    @lru_cache(maxsize=1024)
    def uniquePaths2(self, m: int, n: int) -> int: 

        dp = [[0]*(n + 1) for _ in range(m + 1)]

        def helper(m, n):
            if m == 1 or n == 1:
                return 1
            if dp[m][n]:
                return dp[m][n]
            dp[m][n] = helper(m - 1, n) + helper(m, n - 1)
            return dp[m][n]

        return helper(m, n)

    
# Iteration + Tabulation
# O(m*n) time, O(m*n) space
    def uniquePaths3(self, m: int, n: int) -> int: 

        dp = [[1]*n for _ in range(m)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]

    
# Iteration + Tabulation (Optimized)
# O(m*n) time, O(n) space
    def uniquePaths4(self, m: int, n: int) -> int: 

        dp = [[1]*n for _ in range(2)]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[0][j] = dp[1][j] + dp[0][j + 1]
            dp[1] = dp[0]
        return dp[0][0]

    
# Iteration + Tabulation (Extra Optimized)
# O(m*n) time, O(n) space
    def uniquePaths(self, m: int, n: int) -> int: 

        dp = [1]*n

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[j] = dp[j] + dp[j + 1]
        return dp[0]

    
    # Math solution
    def uniquePaths5(self, m: int, n: int) -> int:
        import math
        return math.comb(n + m - 2, m - 1)


#         28 21 15 10 6  3  1 
#         7  6  5  4  3  2  1
#         1  1  1  1  1  1  1