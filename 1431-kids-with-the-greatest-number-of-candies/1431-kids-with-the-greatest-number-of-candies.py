class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        res = [False]*len(candies)
        for i, c in enumerate(candies):
            if c + extraCandies >= mx:
                res[i] = True
        return res