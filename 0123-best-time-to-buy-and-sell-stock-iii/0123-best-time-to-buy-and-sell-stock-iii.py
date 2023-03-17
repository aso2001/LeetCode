class Solution:
# Using State Machine
    def maxProfit(self, prices: List[int]) -> int:

        c1, p1, c2, p2 = math.inf, 0, math.inf, 0

        for i in range(len(prices)):
            c1 = min(c1, prices[i])
            p1 = max(p1, prices[i] - c1)
            c2 = min(c2, prices[i] - p1)
            p2 = max(p2, prices[i] - c2)
        return max(0, p2)
    
    
    def maxProfit2(self, prices: List[int]) -> int:
        p = prices
        ln = len(p)

        mini = [10**6, -1]
        maxi = [-1, -1]

        for i in range(ln):
            if p[i] < mini[0]:
                mini = [p[i], i]
            if p[i] - mini[0] > maxi[0]:
                maxi = [p[i] - mini[0], i]
        
        if maxi[1] < mini[1]:
            mini = [10**6, -1]
            for i in range(maxi[1]):
                if p[i] < mini[0]:
                    mini = [p[i], i]
            
        mini1, maxi1 = 10**6, -1
        if maxi[0] > 0:
            for i in range(maxi[1], mini[1] - 1, -1):
                mini1 = min(mini1, p[i])
                maxi1 = max(maxi1, p[i] - mini1)

        mini2, maxi2 = 10**6, -1
        if mini[1] > 0:
            for i in range(mini[1]):
                mini2 = min(mini2, p[i])
                maxi2 = max(maxi2, p[i] - mini2)

        mini3, maxi3 = 10**6, -1
        if maxi[1] < ln - 1:
            for i in range(maxi[1]+1, ln):
                mini3 = min(mini3, p[i])
                maxi3 = max(maxi3, p[i] - mini3)

        print(maxi[0],maxi1,maxi2,maxi3)
        print(mini[0], mini1)
        maxx = max(maxi[0], maxi1 + maxi[0], maxi[0] + maxi2, maxi[0] + maxi3)
        return maxx