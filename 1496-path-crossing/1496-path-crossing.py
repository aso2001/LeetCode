class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cur = (0, 0)
        visited = set()
        visited.add(cur)
        for c in path:
            if c == 'N':
                cur = (cur[0], cur[1] + 1)
            elif c == 'S':
                cur = (cur[0], cur[1] - 1)
            elif c == 'W':
                cur = (cur[0] - 1, cur[1])
            elif c == 'E':
                cur = (cur[0] + 1, cur[1])
            if cur in visited:
                return True
            visited.add(cur)
        return False