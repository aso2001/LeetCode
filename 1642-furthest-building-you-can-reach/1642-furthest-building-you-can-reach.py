class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        q = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
            bricks -= diff
            heapq.heappush(q, -diff)
            if bricks < 0:
                if ladders:
                    ladders -= 1
                    if q:
                        bricks -= heapq.heappop(q)
                else:
                    return i
        return len(heights) - 1