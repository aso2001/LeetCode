class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lr = len(board)
        lc = len(board[0])

        # 0, 1: dead, live
        # 2: 0 -> 1 dead -> live
        # 3: 1 -> 0 live -> dead

        nbr = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        for i in range(lr):
            for j in range(lc):
                cnt = 0
                for k in nbr:
                    if 0 <= i + k[0] < lr and 0 <= j + k[1] < lc:
                        cnt += board[i+k[0]][j+k[1]]%2
                if board[i][j] == 1:
                    if cnt < 2 or cnt > 3: board[i][j] = 3
                else:
                    if cnt == 3: board[i][j] = 2
        
        #print(board)
        for i in range(lr):
            for j in range(lc):
                if board[i][j] == 3: board[i][j] = 0
                elif board[i][j] == 2: board[i][j] = 1