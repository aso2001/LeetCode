class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        
        dp = [[0]*len(pizza[0]) for _ in range(len(pizza))]

        for i in range(len(dp) - 1, -1, -1):
            for j in range(len(dp[0]) - 1, -1, -1):
                if i < len(dp) - 1 and j < len(dp[0]) - 1:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1] - dp[i + 1][j + 1] + (pizza[i][j] == 'A')
                elif i == len(dp) - 1 and j < len(dp[0]) - 1:
                    dp[i][j] = dp[i][j + 1] + (pizza[i][j] == 'A')
                elif i < len(dp) - 1 and j == len(dp[0]) - 1:
                    dp[i][j] = dp[i + 1][j] + (pizza[i][j] == 'A')
                elif i == len(dp) - 1 and j == len(dp[0]) - 1:
                    dp[i][j] = (pizza[i][j] == 'A')

        @lru_cache(maxsize = None)
        def dfs(i, j, c):
            if not dp[i][j]:
                return 0
            if c == 1:
                return 1
            res = 0
            for ii in range(i + 1, len(dp)):
                if dp[i][j] - dp[ii][j] > 0:
                    res += dfs(ii, j, c - 1)
            for jj in range(j + 1, len(dp[0])):
                if dp[i][j] - dp[i][jj] > 0:
                    res += dfs(i, jj, c - 1)
            return res

        res = dfs(0, 0, k) % (10**9 + 7)
        return res      