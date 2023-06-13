class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dh = defaultdict(list)
        dv = defaultdict(list)
        for i in range(len(grid)):
            tmp = []
            for j in range(len(grid[0])):
                tmp.append(grid[i][j])
            tmp = tuple(tmp)
            if tmp in dh:
                dh[tmp] += 1
            else: dh[tmp] = 1
        for j in range(len(grid[0])):
            tmp = []
            for i in range(len(grid)):
                tmp.append(grid[i][j])
            tmp = tuple(tmp)
            if tmp in dv:
                dv[tmp] += 1
            else: dv[tmp] = 1
        res = 0
        for i in dh:
            if i in dv:
                res += dh[i]*dv[i]
        return res   