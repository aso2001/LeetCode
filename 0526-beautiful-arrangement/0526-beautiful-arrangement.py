class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        visited = set()

        def dfs(i, visited):
            nonlocal res
            if len(visited) == n:
                res += 1
            
            for j in range(1, n + 1):
                if j not in visited and (i%j == 0 or j%i == 0):
                    visited.add(j)
                    dfs(i + 1, visited)
                    visited.remove(j)

        dfs(1, visited)
        
        return res