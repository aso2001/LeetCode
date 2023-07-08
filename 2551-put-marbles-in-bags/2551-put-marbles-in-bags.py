class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        mx, mn = [], []
        for i in range(len(weights) - 1):
            heapq.heappush(mn, weights[i] + weights[i + 1])
            heapq.heappush(mx, -(weights[i] + weights[i + 1]))
        mxx, mnn = 0, 0
        while k > 1:
            mxx -= heapq.heappop(mx)
            mnn += heapq.heappop(mn)
            k -= 1
        return mxx - mnn