class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Union-Find solution

        parents = {}

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x,y):

            parents.setdefault(x, x)
            parents.setdefault(y, y)

            r1 = find(x)
            r2 = find(y)

            if r1 != r2:
                parents[r2] = r1

        for i, j in stones:
            union(i, ~j)

        roots = set()

        for key in parents:
            root = find(key)
            roots.add(root)
        return len(stones) - len(roots)

    def removeStones1(self, stones: List[List[int]]) -> int:
        # DFS solution to find number of separate graph components
        adj = {i:[] for i in range(len(stones))}

        for i in range(len(stones)):
            x0, y0 = stones[i]
            for j in range(len(stones)):
                if i == j:
                    continue
                x1, y1 = stones[j]
                if x0 == x1 or y0 == y1:
                    adj[i].append(j)  

        def dfs(v, visited):
            q = [v]
            while q:
                cur = q.pop()
                visited.add(cur)
                for nei in adj[cur]:
                    if nei not in visited:
                        q.append(nei)

        cnt, visited = 0, set()
        for v in adj:
            if v not in visited:
                dfs(v, visited)
                cnt += 1
        return len(stones) - cnt

        # 0: 1, 2
        # 1: 0, 4
        # 2: 0, 3
        # 3: 2, 5
        # 4: 1, 5
        # 5: 3, 4