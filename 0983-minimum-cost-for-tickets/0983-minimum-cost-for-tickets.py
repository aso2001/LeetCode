class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = {}
        dayset = set(days)

        def dfs(i):
            if i > 365:
                return 0
            if i in dp:
                return dp[i]
            if i in dayset:
                dp[i] = min(dfs(i + 1) + costs[0], dfs(i + 7) + costs[1], dfs(i + 30) + costs[2])
                return dp[i]
            else:
                return dfs(i + 1)
        
        return dfs(1)