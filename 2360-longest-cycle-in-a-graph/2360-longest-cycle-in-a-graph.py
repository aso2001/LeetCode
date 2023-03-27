class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = [False]*len(edges)
        res = -1
        for i in range(len(edges)):
            seq = []
            while edges[i] != -1 and not visited[i]:
                seq.append(i)
                visited[i] = True
                i = edges[i]
            if i in seq:
                res  = max(res, len(seq) - seq.index(i))
        return res