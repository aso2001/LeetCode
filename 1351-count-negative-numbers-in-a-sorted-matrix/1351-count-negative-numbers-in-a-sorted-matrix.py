class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            L, R = 0, len(grid[0]) - 1
            if grid[i][R] >= 0:
                continue
            while L < R:
                mid = (L + R)//2
                if grid[i][mid] < 0:
                    R = mid
                else:
                    L = mid + 1
            res += len(grid[0]) - L
        return res