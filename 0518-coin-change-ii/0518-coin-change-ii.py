class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {}

        def dfs(a, i):
            if a > amount or i == len(coins):
                return 0
            if a == amount:
                return 1
            if (a, i) in dp:
                return dp[(a, i)]
            
            dp[(a, i)] = dfs(a + coins[i], i) + dfs(a, i + 1)
            return dp[(a, i)]
        
        return dfs(0, 0)


    def change2(self, amount: int, coins: List[int]) -> int:

        # TLE
        # C(N, m) = C(N, m-1) + C(N-S_m, m)

        if amount < 0 or len(coins) <= 0:
            return 0
        if amount == 0:
            return 1

        return self.change(amount, coins[:-1]) + self.change(amount - coins[-1], coins)