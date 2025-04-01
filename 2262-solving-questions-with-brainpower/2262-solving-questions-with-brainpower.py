class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        q = questions

        dp = [-1]*len(q)

        def dfs(i):
            if i >= len(q):
                return 0
            if dp[i] != -1:
                return dp[i]
            else:
                dp[i] = max(q[i][0] + dfs(i + q[i][1] + 1), dfs(i + 1))
            return dp[i]

        return dfs(0)