class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        import heapq
        hh = [-s for s in stones]
        heapq.heapify(hh)

        while hh:
            h1 = heapq.heappop(hh)
            if not len(hh):
                return -h1
            h2 = heapq.heappop(hh)
            if h1 == h2:
                continue
            else:
                h1 = h1 - h2
                heapq.heappush(hh, h1)
        return 0