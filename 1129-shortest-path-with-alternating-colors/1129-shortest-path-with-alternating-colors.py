class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        red = defaultdict(list)
        blue = defaultdict(list)
        for b, e in redEdges:
            red[b].append(e)
        for b, e in blueEdges:
            blue[b].append(e)

        q = deque()
        q.append((0, None, 0))
        res = [-1]*n
        visited = set()
        visited.add((0, None))

        while q:
            cur, col, lev = q.popleft()
            if res[cur] == -1:
                res[cur] = lev
            if col != 'r':
                for nei in red[cur]:
                    if (nei, 'r') not in visited:
                        q.append((nei, 'r', lev + 1))
                        visited.add((nei, 'r'))
            if col != 'b':
                for nei in blue[cur]:
                    if (nei, 'b') not in visited:
                        q.append((nei, 'b', lev + 1))
                        visited.add((nei, 'b'))
        return res