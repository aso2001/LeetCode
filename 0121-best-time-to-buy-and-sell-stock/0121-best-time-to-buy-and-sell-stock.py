class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini = 10**5
        maxi = 0
        for p in prices:
            if p < mini:
                mini = p
            if p - mini > maxi:
                maxi = p - mini
        return maxi


    #Using State Machine
    def maxProfit2(self, prices: List[int]) -> int:
        max1 = -prices[0]
        max2 = 0
        for i in range(1, len(prices)):
            max1 = max(max1, -prices[i])
            max2 = max(max2, max1 + prices[i])
        return max(0, max2)


    def maxProfit3(self, prices: List[int]) -> int:
        minp = prices[0]
        maxp = 0
        for i in range(1,len(prices)):
            if prices[i] > minp:
                if maxp < prices[i] - minp:
                    maxp = prices[i] - minp
            else:
                minp = prices[i]
        return maxp


    def maxProfit4(self, prices: List[int]) -> int:

        mini = 10**5
        maxi = 0
        for p in prices:
            mini = min(mini, p)
            maxi = max(maxi, p - mini)
        return maxi







































    def maxProfit2(self, prices: List[int]) -> int:

        mini = 10**5
        maxi = 0
        for p in prices:
            mini = min(mini, p)
            maxi = max(maxi, p - mini)
        return maxi