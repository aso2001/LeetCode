class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        # DP solution
        tot = sum(piles)
        dp = [[0]*len(piles) for _ in range(len(piles))]

        def stones(L, R):
            if L < len(piles) and dp[L][R] != 0:
                return dp[L][R]
            if L > R:
                return 0
            
            left = piles[L] if (R - L)%2 else 0
            right = piles[R] if (R - L)%2 else 0
            dp[L][R] = max(stones(L + 1, R) + left, stones(L, R - 1) + right)
            return dp[L][R]

        return stones(0, len(piles) - 1) >= tot//2

    def stoneGame2(self, piles: List[int]) -> bool:
        # Alice always wins
        return True