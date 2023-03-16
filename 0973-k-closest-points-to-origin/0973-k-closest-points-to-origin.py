class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        res, hh = [], []
        for p in points:
            dist = p[0]*p[0] + p[1]*p[1]
            hh.append([dist, p])
        heapq.heapify(hh)
        for _ in range(k):
            tmp = heapq.heappop(hh)
            res.append(tmp[1])
        return res

