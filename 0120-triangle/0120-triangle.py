class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = triangle[len(triangle) - 1]

        for j in range(len(triangle) - 2, -1, -1):
            for i in range(j + 1):
                dp[i] = triangle[j][i] + min(dp[i], dp[i + 1])
        return dp[0]