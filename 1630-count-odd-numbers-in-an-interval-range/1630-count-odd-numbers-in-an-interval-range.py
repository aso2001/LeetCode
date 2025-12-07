class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + low%2 + high%2)//2

        # 1 3 5 7 9 11 13