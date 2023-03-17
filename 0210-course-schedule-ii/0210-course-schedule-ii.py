class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nc = numCourses
        visited, cycle = set(), set()
        res = []

        G = {i:[] for i in range(nc)}
        for c, pre in prerequisites:
            G[c].append(pre)

        def dfs(c):
            if c in cycle:
                return False

            if c in visited:
                return True

            cycle.add(c)
            for pre in G[c]:
                if not dfs(pre):
                    return True
            cycle.remove(c)
            visited.add(c)
            res.append(c)
            return True

        for c in G:
            if not dfs(c):
                return []
        return res