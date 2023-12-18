class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        mx = matrix
        res = 0
        for i in range(len(mx)):
            px = 0
            for j in range(len(mx[0])):
                if mx[i][j] == 1 and i > 0:
                    mx[i][j] += mx[i - 1][j]
            cur_row = sorted(mx[i], reverse=True)
            for i in range(len(mx[0])):
                res = max(res, cur_row[i] * (i + 1))
        return res