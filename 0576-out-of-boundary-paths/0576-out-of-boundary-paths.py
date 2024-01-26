class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9 + 7
        dp = [[[0]*n for _ in range(m)] for _ in range(maxMove + 1)]

        def dfs(x, y, remain):
            if x < 0 or y < 0 or x == m or y == n:
                return 1
            if remain <= x and remain <= y and x + remain < m and y + remain < n:
                return 0
            if dp[remain][x][y] == 0:
                dp[remain][x][y] = (dfs(x - 1, y, remain - 1) + dfs(x + 1, y, remain - 1) + dfs(x, y - 1, remain - 1) + dfs(x, y + 1, remain - 1)) % mod
            return dp[remain][x][y]
        
        dfs(startRow, startColumn, maxMove)
        return dp[maxMove][startRow][startColumn]