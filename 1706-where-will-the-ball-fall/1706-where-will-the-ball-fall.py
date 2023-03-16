class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = []

        def trans(state):
            (i, j, side) = state
            if side == 'up':
                if grid[i][j] == 1:
                    return((i, j + 1, 'left'))
                else: # if grid[i][j] == -1:
                    return((i, j - 1, 'right'))
            elif side == 'left':
                if grid[i][j] == 1:
                    return((i + 1, j, 'up'))
                else:
                    return((i, j, 'stop'))
            else: #if side == 'right':
                if grid[i][j] == 1:
                    return((i, j, 'stop'))
                else:
                    return((i + 1, j, 'up'))

        for j in range(len(grid[0])):
            state = (0, j, 'up')
            while state[0] < len(grid) and state[1] >= 0 and state[1] != len(grid[0]) and state[2] != 'stop':
                state = trans(state)
            if state[1] < 0 or state[1] == len(grid[0]) or state[2] == 'stop':
                res.append(-1)
                continue
            res.append(state[1])
        return res