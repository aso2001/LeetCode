class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        dd = {}
        for i in range(len(wall)):
            st = 0
            for j in range(len(wall[i])):
                st += wall[i][j]
                if st in dd:
                    dd[st] += 1
                else:
                    dd[st] = 1

        del dd[sum(wall[0])]
        return len(wall) - max(dd.values()) if dd else len(wall)