class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = [[-1]*len(matrix[0]) for _ in range(len(matrix))]

        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] <= prev:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = 1 + max(dfs(i + 1, j, matrix[i][j]), dfs(i - 1, j, matrix[i][j]), dfs(i, j + 1, matrix[i][j]), dfs(i, j - 1, matrix[i][j]))
            return dp[i][j]

        res = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res = max(res, dfs(i, j, -1))
        return res