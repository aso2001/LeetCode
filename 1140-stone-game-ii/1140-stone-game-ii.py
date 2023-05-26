class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = defaultdict(list)

        def dfs(i, m):
            if 2*m >= len(piles) - i:
                return sum(piles[i:])
            elif (i, m) in dp:
                return dp[(i, m)]
            res = 0
            for j in range(1, 2*m + 1):
                res = max(res, sum(piles[i:]) - dfs(i + j, max(j, m)))
                dp[(i, m)] = res
            return dp[(i, m)]
        
        return dfs(0, 1)     