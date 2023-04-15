class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)

        dp = [[-1]*(k + 1) for _ in range(n)]

        def dfs(i, cnt):
            if i == n:
                return 0
            if dp[i][cnt] != -1:
                return dp[i][cnt]

            dp[i][cnt] = dfs(i + 1, cnt)
            curPile = 0
            for j in range(min(cnt, len(piles[i]))):
                curPile += piles[i][j]
                dp[i][cnt] = max(dp[i][cnt], curPile + dfs(i + 1, cnt - j - 1))
            return dp[i][cnt]

        return dfs(0, k)