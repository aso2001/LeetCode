class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        move = [(0,1), (0,-1), (1,0), (-1,0)]
        vo = []

        for i in range(len(board)):
            if board[i][0] == 'O':
                vo.append((i, 0))
            if board[i][len(board[0]) - 1] == 'O':
                vo.append((i, len(board[0]) - 1))
        for j in range(1, len(board[0]) - 1):
            if board[0][j] == 'O':
                vo.append((0, j))
            if board[len(board) - 1][j] == 'O':
                vo.append((len(board) - 1, j))

        while vo:
            (i, j) = vo.pop(0)
            if board[i][j] == 'O':
                board[i][j] = 'Y'   # paint by 'Y' all 'O' cells conected to border 'O' cells
                for mm in move:               
                    di, dj = mm[0], mm[1]
                    if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]):
                        vo.append((i + di, j + dj))         # add to queue all neighbors of (i, j) cell

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'Y':
                    board[i][j] = 'O'
