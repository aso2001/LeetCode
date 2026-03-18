#translated using AI
class Solution:
    def countSubmatrices(self, grid, k):
        n, m = len(grid), len(grid[0])

        prefix = [0] * m
        ans = 0

        for i in range(n):
            rowSum = 0
            for j in range(m):
                rowSum += grid[i][j]
                prefix[j] += rowSum

                if prefix[j] <= k:
                    ans += 1

        return ans