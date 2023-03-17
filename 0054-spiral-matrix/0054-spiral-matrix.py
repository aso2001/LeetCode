class Solution:
    def spiralOrder(self, mx: List[List[int]]) -> List[int]:
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