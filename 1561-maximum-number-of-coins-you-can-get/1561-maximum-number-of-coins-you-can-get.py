class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        res = 0
        for i in range(1,len(piles)*2//3,2):
            res += piles[i]
        return res