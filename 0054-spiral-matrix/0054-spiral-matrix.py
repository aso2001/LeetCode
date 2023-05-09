class Solution:
    def spiralOrder(self, mx: List[List[int]]) -> List[int]:
        cnt = 0
        res = []
        L, R, U, D = 0, len(mx[0]) - 1, 0, len(mx) - 1
        while True:
            for j in range(L, R + 1):
                res.append(mx[U][j])
                cnt += 1
            if cnt == len(mx[0])*len(mx):
                break
            for i in range(U + 1, D + 1):
                res.append(mx[i][R])
                cnt += 1
            if cnt == len(mx[0])*len(mx):
                break
            for j in range(R - 1, L - 1, -1):
                res.append(mx[D][j])
                cnt += 1
            if cnt == len(mx[0])*len(mx):
                break
            for i in range(D - 1, U, -1):
                res.append(mx[i][L])
                cnt += 1
            if cnt == len(mx[0])*len(mx):
                break
            U += 1
            D -= 1
            L += 1
            R -= 1
        return res
    
    
    def spiralOrder2(self, mx: List[List[int]]) -> List[int]:
        res, i1, i2, j1, j2 = [], 0, len(mx), 0, len(mx[0])

        while True:
            if j1 >= j2: break
            for j in range(j1, j2):
                res.append(mx[i1][j])
            i1 += 1
            if i1 >= i2: break
            for i in range(i1, i2):
                res.append(mx[i][j])
            j2 -= 1
            if j2 <= j1: break
            for j in range(j2 - 1, j1 - 1, -1):
                res.append(mx[i][j])
            i2 -= 1
            if i2 <= i1: break
            for i in range(i2 - 1, i1 - 1, -1 ):
                res.append(mx[i][j])
            j1 += 1
        return res