class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}
        sqrs = []
        mnsqr = int(sqrt(n))
        if mnsqr == sqrt(n): return 1
        for i in range(1, mnsqr + 1):
            sqrs.append(i*i)
        sq = set(sqrs)

        def dfs(i):
            if i in sq:
                dp[i] = 1
                return 1
            if i in dp:
                return dp[i]
            dp[i] = math.inf
            for j in sqrs:
                if i - j < 0:
                    break
                dp[i] = min(1 + dfs(i - j), dp[i])
            return dp[i]
        return dfs(n)

    def numSquares2(self, n: int) -> int:
        dp = {}
        sq = []
        if int(sqrt(n)) == sqrt(n): return 1 
        mxn = int(sqrt(n))
        for i in range(1, mxn + 1):
            sq.append(i*i)
        sqs = set(sq)

        def dfs(i):
            if i in sqs:
                dp[i] = 1
                return 1
            if i in dp:
                return dp[i]
            dp[i] = math.inf
            for s in sq:
                if s > i:
                    break
                dp[i] = min(dp[i], dfs(i - s) + 1)
            return dp[i]

        return dfs(n)