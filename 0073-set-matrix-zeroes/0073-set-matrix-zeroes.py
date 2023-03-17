class Solution:
    def setZeroes(self, mx: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # O(1) using first "0" raw and "0" colomn to mark with 'x' other "0" colomns and raws
        flag = 0
        for i in range(len(mx)):
            for j in range(len(mx[0])):
                if mx[i][j] == 0:
                    if flag == 0:
                        xr = i
                        xc = j
                        flag = 1
                    mx[xr][j] = 'x'
                    mx[i][xc] = 'x'
        # print(mx)
        if flag == 1:
            for i in range(len(mx)):
                for j in range(len(mx[0])):
                    if j == xc or i == xr:
                        continue
                    if mx[i][xc] == 'x' or mx[xr][j] == 'x':
                        mx[i][j] = 0
            for i in range(len(mx)):
                mx[i][xc] = 0
            for j in range(len(mx[0])):
                mx[xr][j] = 0
                
                
    def setZeroes2(self, mx: List[List[int]]) -> None:
        # O(m + n) using sets
        col, raw = set(), set()
        for i in range(len(mx)):
            for j in range(len(mx[0])):
                if mx[i][j] == 0:
                    raw.add(i)
                    col.add(j)
        for i in raw:
            for j in range(len(mx[0])):
                mx[i][j] = 0
        for j in col:
            for i in range(len(mx)):
                mx[i][j] = 0