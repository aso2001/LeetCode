class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        pt = 0
        for i in range(1, len(prices)):
            pt += max(prices[i] - prices[i - 1], 0)
        return pt