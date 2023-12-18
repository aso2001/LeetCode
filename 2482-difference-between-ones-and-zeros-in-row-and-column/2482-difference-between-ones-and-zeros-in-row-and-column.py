class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        r1, c1 = [0]*n, [0]*m
        diff = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    c1[j] += 1
                    r1[i] += 1
        for i in range(n):
            for j in range(m):
                diff[i][j] = 2*(r1[i] + c1[j]) - n - m
        return diff