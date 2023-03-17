class Solution:
    def maxArea(self, h: List[int]) -> int:
        i, j = 0, len(h) - 1

        maxw = min(h[i], h[j])*(j - i)
        while i != j:
            maxw = max(maxw, min(h[i], h[j])*(j - i))
            if h[i] > h[j]:
                j -= 1
            else:
                i += 1
        return maxw