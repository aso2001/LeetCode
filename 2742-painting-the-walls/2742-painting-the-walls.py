class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n + 1)
        prev_dp = [inf]*(n + 1)
        prev_dp[0] = 0

        for i in range(n - 1, -1, -1):
            dp = [0]*(n + 1)
            for rem in range(1, n + 1):
                paint = cost[i] + prev_dp[max(0, rem - 1 - time[i])]
                dont_paint = prev_dp[rem]
                dp[rem] = min(paint, dont_paint)
            prev_dp = dp
        return dp[n]