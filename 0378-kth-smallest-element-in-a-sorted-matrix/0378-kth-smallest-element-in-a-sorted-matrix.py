class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        hh = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heapq.heappush(hh, -matrix[i][j])
                if len(hh) > k:
                    heapq.heappop(hh)
        return -heapq.heappop(hh)