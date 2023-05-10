class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0]*n for _ in range(n)]
        cnt, L, R, U, D = 0, 0, n - 1, 0, n - 1
        while True:
            for j in range(L, R + 1):
                cnt += 1
                res[U][j] = cnt
            for i in range(U + 1, D + 1):
                cnt += 1
                res[i][R] = cnt
            for j in range(R - 1, L - 1, -1):
                cnt += 1
                res[D][j] = cnt
            for i in range(D - 1, U, -1):
                cnt += 1
                res[i][L] = cnt
            L += 1
            R -= 1
            U += 1
            D -= 1
            if U > D or L > R:
                break
        return res   