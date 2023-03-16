class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        cols, rows = len(heights[0]), len(heights)

        def dfs(r, c, visited, prevHeight):
            if r == rows or c == cols or r < 0 or c < 0 or heights[r][c] < prevHeight or (r, c) in visited:
                return
            visited.add((r, c))
            moves = {(0, -1), (0, 1), (-1, 0), (1, 0)}
            for mm in moves:
                dfs(r + mm[0], c + mm[1], visited, heights[r][c])
    
        pac, atl = set(), set()
        for i in range(rows):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, cols - 1, atl, heights[i][cols - 1])
        
        for j in range(cols):
            dfs(0, j, pac, heights[0][j])
            dfs(rows - 1, j, atl, heights[rows - 1][j])

        res = []
        for p in pac:
            if p in atl:
                res.append(p)
        return res
    

    def pacificAtlantic2(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        dd = {}
        moves = {(0, -1), (0, 1), (-1, 0), (1, 0)}
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                nei = []
                for mm in moves:
                    if 0 <= i + mm[0] < len(heights)  and 0 <= j + mm[1] < len(heights[0]) and heights[i][j] >= heights[i + mm[0]][j + mm[1]]:
                        nei.append((i + mm[0], j + mm[1])) 
                dd[(i, j)] = nei

        for d in dd:
            fA, fP = 0, 0
            nei = dd[d].copy()
            nei.append(d)
            visited = []
            while nei:
                cur = nei.pop()
                visited.append(cur)
                if cur[0] == len(heights) - 1 or cur[1] == len(heights[0]) - 1:
                    fA = 1
                if cur[0] == 0 or cur[1] == 0:
                    fP = 1
                if fA*fP:
                    res.append([d[0], d[1]])
                    break
                if dd[cur]:
                    for nn in dd[cur]:
                        if nn not in visited and nn not in nei:
                            nei.append(nn)
        return res