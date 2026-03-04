class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        r = [0]*n
        c = [0]*m
        for i in range(n):
            for j in range(m):
                if mat[i][j]:
                    r[i] += 1
                    c[j] += 1
        res = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j]:
                    if r[i] == 1 and c[j] == 1:
                        res += 1
        return res