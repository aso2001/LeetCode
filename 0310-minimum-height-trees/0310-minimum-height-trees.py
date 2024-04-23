class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # res = []
        # for root in range(n):
        #     q = deque([(root, 1)])
        #     visited = set()
        #     while q:
        #         cur, height = q.popleft()
        #         visited.add(cur)
        #         for chd in adj[cur]:
        #             if chd not in visited:
        #                 q.append((chd, height + 1))
        #     res.append((height, root))

        # res.sort()
        # ans = [res[0][1]]
        # for r in res[1:]:
        #     if r[0] == res[0][0]:
        #         ans.append(r[1])
        # return ans
    
        if n == 1: return [0]
        leaves = [node for node in range(n) if len(adj[node]) == 1]
        remaining_nodes = n

        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                nei = adj[leaf][0]
                adj[nei].remove(leaf)
                if len(adj[nei]) == 1:
                    new_leaves.append(nei)
            leaves = new_leaves
        return leaves