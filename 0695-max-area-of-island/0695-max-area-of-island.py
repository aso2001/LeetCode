class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # BFS iterative
        move = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island = [(i, j)]
                    cnt = 0
                    while island:
                        cur = island.pop()
                        grid[cur[0]][cur[1]] = 0  # Mark visited cells with '0'
                        cnt += 1
                        for mm in move:
                            if 0 <= cur[0] + mm[0] < len(grid) and 0 <= cur[1] + mm[1] < len(grid[0]) and grid[cur[0] + mm[0]][cur[1] + mm[1]] == 1:
                                tmp = (cur[0] + mm[0], cur[1] + mm[1])
                                island.append(tmp)
                                grid[tmp[0]][tmp[1]] = 0  # Mark visited cells with '0'
                    maxArea = max(maxArea, cnt)
        
        return maxArea

        # stack = []
        # move = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == 1:
        #             stack.append((i, j))

        # maxArea = 0
        # while stack:
        #     cur = stack.pop()
        #     island = [cur]
        #     cnt = 0
        #     while island:
        #         cur = island.pop()
        #         grid[cur[0]][cur[1]] = 0  # Mark visited cells with '0'
        #         cnt += 1
        #         for mm in move:
        #             if 0 <= cur[0] + mm[0] < len(grid) and 0 <= cur[1] + mm[1] < len(grid[0]) and grid[cur[0] + mm[0]][cur[1] + mm[1]] == 1:
        #                 tmp = (cur[0] + mm[0], cur[1] + mm[1])
        #                 island.append(tmp)
        #                 grid[tmp[0]][tmp[1]] = 0  # Mark visited cells with '0'
        #                 stack.remove(tmp)
        #     maxArea = max(maxArea, cnt)
        
        # return maxArea