class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        import heapq
        grid = set()
        for i in range(len(buildings)):
            grid.add(buildings[i][0])
            grid.add(buildings[i][1])
        grid = list(grid)
        grid.sort()
        res, h, j = [], [], 0
        for g in grid:
            while j < len(buildings) and buildings[j][0] <= g:
                heapq.heappush(h, (-buildings[j][2], buildings[j][1]))
                hh = buildings[j][2]
                j += 1
            while h and h[0][1] <= g:
                hh = -h[0][0]
                heapq.heappop(h)
            if h:
                hh = -h[0][0]
            else:
                hh = 0
            if res:
                if res[-1][1] == hh:
                    continue
            res.append([g, hh])
        return res