class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # BFS solution
        nn = len(board)
        lb, cnt = [], 0
        for i in range(len(board) - 1, -1, -1):
            cnt += 1
            lb = lb + board[i] if cnt%2 else lb + board[i][::-1]   # convert board into 1D list

        q, nxt, nxtp, visited, res = [0], [], [], [], 0
        while True:
            res += 1
            while q:
                cur = q.pop()
                visited.append(cur)
                for n in range(1,7):
                    if cur + n == nn*nn - 1:
                        return res
                    if lb[cur + n] == -1:
                        if cur + n not in nxt and cur + n not in visited:
                            nxt.append(cur + n)
                    else:
                        if cur == lb[cur + n] - 1: # skip position which ends at snake where tail is at current position (snake loop)
                            continue
                        if lb[cur + n] == nn*nn:
                            return res
                        if lb[cur + n] - 1 not in nxt and lb[cur + n] - 1 not in visited:
                            nxt.append(lb[cur + n] - 1)
            if nxtp == nxt:
                return -1
            nxtp = nxt
            q = nxt.copy()
            nxt = []