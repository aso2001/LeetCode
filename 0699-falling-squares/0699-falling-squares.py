class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        p = positions
        grid = set()
        for i in range(len(p)):
            grid.add(p[i][0] + 0.5)
            grid.add(p[i][0] + p[i][1] - 0.5)
        grid = list(grid)
        grid.sort()

        res, mxx = [], 0
        gh = [0]*len(grid)
        for i in range(len(p)):
            l, r = p[i][0] + 0.5, p[i][0] + p[i][1] - 0.5   # set left and right centroid for interval affected by falling square

            start = grid.index(l)
            j = start
            mx = gh[j]
            while grid[j] < r:      # find maximum height for affected interval
                j += 1
                mx = max(mx, gh[j])

            j = start
            while grid[j] < r:      # set new height for affected interval as (mx + cube size)
                gh[j] = mx + p[i][1]
                j += 1
            gh[j] = mx + p[i][1]

            mxx = max(mxx, mx + p[i][1]) # keep track of maximum height stack
            res.append(mxx)
        return res