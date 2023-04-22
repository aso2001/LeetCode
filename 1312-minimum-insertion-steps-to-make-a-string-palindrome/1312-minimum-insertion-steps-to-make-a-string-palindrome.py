class Solution:
    def minInsertions(self, s: str) -> int:
        
        dp = [[-1]*501 for _ in range(501)]
        def dfs(i, j):
            if i == j or (i == j - 1 and s[i] == s[j]):
                return 0
            elif dp[i][j] != -1:
                return dp[i][j]
            elif s[i] == s[j]:
                return dfs(i + 1, j - 1)
            elif s[i] != s[j]:
                dp[i][j] = 1 + min(dfs(i, j - 1), dfs(i + 1, j))
            return dp[i][j]

        return dfs(0, len(s) - 1)