class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(list)
        for a, b, c in roads:
            if a not in d:
                d[a] = [(b, c)]
            else:
                d[a].append((b, c))
            if b not in d:
                d[b] = [(a, c)]
            else:
                d[b].append((a, c))

        visited = [False]*n
        res = []
        q = deque()
        q.append(1)

        while q:
            cur = q.popleft()
            if not visited[cur - 1]:
                visited[cur - 1] = True
                for nei in d[cur]:
                    if not visited[nei[0] - 1]:
                        res.append(nei[1])
                        q.append(nei[0])
        return min(res)