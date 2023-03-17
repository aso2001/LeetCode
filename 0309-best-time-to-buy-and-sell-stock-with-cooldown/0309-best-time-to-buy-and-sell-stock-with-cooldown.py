class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, buying) val=max_profit

        def trans(i, buying):
            if i >= len(prices):
                return 0

            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                dp[(i, buying)] = max(trans(i + 1, buying), trans(i + 1, not buying) - prices[i])
            else:
                dp[(i, buying)] = max(trans(i + 1, buying), trans(i + 2, not buying) + prices[i])
            return dp[(i, buying)]

        return trans(0, True)