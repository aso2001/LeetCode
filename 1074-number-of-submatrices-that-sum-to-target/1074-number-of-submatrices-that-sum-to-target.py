class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        pfx = [[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                pfx[i][j] = matrix[i][j] + (0 if not i else pfx[i - 1][j]) + (0 if not j else pfx[i][j - 1]) - (pfx[i - 1][j - 1] if i and j else 0)

        res = 0
        for r1 in range(n):
            for r2 in range(r1, n):
                dd = defaultdict(int)
                dd[0] = 1
                for c in range(m):
                    cur_sum = pfx[r2][c] - (pfx[r1 - 1][c] if r1 else 0)
                    res += dd[cur_sum - target]
                    dd[cur_sum] += 1
        return res

        # TLE
        # res = 0
        # for c1 in range(m):
        #     for r1 in range(n):
        #         for c2 in range(c1, m):
        #             for r2 in range(r1, n):
        #                 mtx2 = pfx[r2][c2] - (pfx[r2][c1 - 1] if c1 else 0) - (pfx[r1 - 1][c2] if r1 else 0) + (pfx[r1 - 1][c1 - 1] if r1 and c1 else 0)
        #                 if mtx2 == target:
        #                     res += 1
        # return res