class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        d = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':continue
                xx = 100*(i//3+1) + j//3
                if xx not in d:
                    d[xx] = [board[i][j]]
                else:
                    if board[i][j] in d[xx]:
                        return False
                    else:
                        d[xx].append(board[i][j])
                if i not in d:
                    d[i] = [board[i][j]]
                else:
                    if board[i][j] in d[i]:
                        return False
                    else:
                        d[i].append(board[i][j])
                if j + 9 not in d:
                    d[j + 9] = [board[i][j]]
                else:
                    if board[i][j] in d[j + 9]:
                        return False
                    else:
                        d[j + 9].append(board[i][j])
        return True
                    
        # i//3 j//3
        # 0 - 8 9 - 17 # d[i] d[j+9]
        # 101 102 103 201 202 203 301 302 303 # d[i//3*100+j//3]