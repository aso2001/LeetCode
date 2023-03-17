class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS solution
        nc = numCourses
        d = {}
        for i in range(nc):     
            d[i] = []
        for e in prerequisites:
            d[e[0]].append(e[1])

        visited = set()

        def dfs(c):
            if c in visited:
                return False
            if d[c] == []:
                return True
            visited.add(c)
            for nei in d[c]:
                if not dfs(nei):
                    return False
            visited.remove(c)
            d[c] = []
            return True
        
        for c in range(nc):
            if not dfs(c):
                return False
        return True