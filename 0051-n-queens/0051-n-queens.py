class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, pdi, ndi = set(), set(), set()

        chessboard = [['.']*n for _ in range(n) ]
        res = []

        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in chessboard])
                return
            for c in range(n):
                if c in col or (r + c) in pdi or (r - c) in ndi:
                    continue
                col.add(c)
                pdi.add(r + c)
                ndi.add(r - c)
                chessboard[r][c] = 'Q'

                backtrack(r + 1)

                col.remove(c)
                pdi.remove(r + c)
                ndi.remove(r - c)
                chessboard[r][c] = '.'

        backtrack(0)
        return res