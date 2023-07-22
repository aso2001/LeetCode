class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, -1), (2, 1), (-2, -1), (-2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]

        dp = [[[0]*n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1

        for kk in range(1, k + 1):
            for i in range(n):
                for j in range(n):
                    for m in moves:
                        if 0 <= i + m[0] < n and 0 <= j + m[1] < n:
                            dp[kk][i][j] += dp[kk - 1][i + m[0]][j + m[1]]
                    dp[kk][i][j] /= 8
                    
        res = sum(dp[k][i][j] for i in range(n) for j in range(n))
        return res