class Solution:
    def find_max(self, grid, x, y):
        mx = 0
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                mx = max(mx, grid[i][j])
        return mx

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        
        mxl = [[0] * (N - 2) for _ in range(N - 2)]
        for i in range(N - 2):
            for j in range(N - 2):
                mxl[i][j] = self.find_max(grid, i, j)
        return mxl