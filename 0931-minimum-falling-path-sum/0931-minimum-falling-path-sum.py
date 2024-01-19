class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = matrix.copy()
        for i in range(1, n):
            for j in range(n):
                dp[i][j] = matrix[i][j] + min(math.inf if j == 0 else dp[i - 1][j - 1], dp[i - 1][j], math.inf if j == n -1 else dp[i -1][j + 1])
        
        res = math.inf
        for j in range(n):
            res = min(res, dp[n - 1][j])
        return res