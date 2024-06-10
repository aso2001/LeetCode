class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_sorted = heights.copy()
        heights_sorted.sort()
        res = 0
        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                res += 1
        return res