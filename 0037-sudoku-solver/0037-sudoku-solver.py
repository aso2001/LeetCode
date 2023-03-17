class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = [set() for _ in range(10)]
        cols = [set() for _ in range(10)]
        boxs = [set() for _ in range(10)]
        q = []
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    rows[r].add(int(board[r][c]))
                    cols[c].add(int(board[r][c]))
                    boxs[3*(r//3) + c//3].add(int(board[r][c]))
                else:
                    q.append((r, c))
        
        def backtrack(n):
            nonlocal solved
            if n == len(q):
                solved = True
                return
            (r, c) = q[n]
            for i in range(1,10):
                if i in rows[r] or i in cols[c] or i in boxs[3*(r//3) + c//3]:
                    continue

                rows[r].add(i)
                cols[c].add(i)
                boxs[3*(r//3) + c//3].add(i)
                board[r][c] = str(i)

                backtrack(n + 1)

                if not solved:
                    rows[r].remove(i)
                    cols[c].remove(i)
                    boxs[3*(r//3) + c//3].remove(i)
                    board[r][c] = '.'
        
        solved = False
        backtrack(0)

        # dd[0 - 8] i
        # dd[9 - 17] 9 + j
        # dd[18 - 26] 18 + i//3*10 + j//3   0   10    20
        #                                   1   11    21
        #                                   2   12    22