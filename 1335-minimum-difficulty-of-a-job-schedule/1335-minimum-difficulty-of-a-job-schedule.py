class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d: return -1

        dp = [[-1]*(d + 1) for _ in range(n + 1)]

        @lru_cache(None)
        def dfs(i, j):
            if dp[i][j] > 0:
                return dp[i][j]
            if j == 1:
                return max(jobDifficulty[i:])
            else:
                cur, res = 0, math.inf
                for ii in range(i, n - j + 1):
                    cur = max(cur, jobDifficulty[ii])
                    res = min(res, cur + dfs(ii + 1, j - 1))
                    dp[i][j] = res
                return res

        return dfs(0, d)