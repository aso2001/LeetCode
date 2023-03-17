class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def maxArea(h):
            h.append(0)
            stack = [-1]
            res = 0

            for i in range(len(h)):
                while h[i] < h[stack[-1]]:
                    hh = h[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, hh*w)
                stack.append(i)
            h.pop()
            return res

        res = 0
        h = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 and matrix[0][j] == '1':
                    h[0][j] = 1
                elif matrix[i][j] == '1':
                    h[i][j] = h[i-1][j] + int(matrix[i][j])
            res = max(res, maxArea(h[i]))
        return res        