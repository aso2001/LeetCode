class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        mx = obstacleGrid
        dp = [[0]*len(mx[0]) for _ in range(len(mx))]

        for i in range(len(mx)):
            for j in range(len(mx[0])):
                if mx[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        if j > 0:
                            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                        else:
                            dp[i][j] = dp[i - 1][j]
                    else:
                        if j > 0:
                            dp[i][j] = dp[i][j - 1]
                        else:
                            dp[0][0] = 1
                            
        return dp[len(mx) - 1][len(mx[0]) - 1]