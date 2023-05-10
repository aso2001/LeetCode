class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mx = matrix
        m, n = len(mx), len(mx[0])
        visited = [[False]*n for _ in range(m)]
        if target < mx[0][0] or target > mx[m - 1][n - 1]:
            return False
        i, j = 0, n - 1
        while 0 <= i < m and 0 <= j < n:
            if visited[i][j]:
                return False
            visited[i][j] = True
            if mx[i][j] == target:
                return True
            elif i < m - 1 and j > 0:
                if target < mx[i][j]:
                    if target < mx[i + 1][j - 1]:
                        j -= 1
                        continue
                    else:
                        i += 1
                        j -= 1
                        continue
                else:
                    if target < mx[i + 1][j]:
                        i += 1
                        j -= 1
                        continue
                    else:
                        i += 1
                        continue
            else:
                if j == 0 and i < m - 1:
                    i += 1
                    continue
                elif i == m - 1 and j > 0:
                    j -= 1
                    continue
        return False 