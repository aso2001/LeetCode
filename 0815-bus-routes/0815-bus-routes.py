class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if target == source: return 0

        adj = defaultdict(list)
        for idx, r in enumerate(routes):
            for st in r:
                adj[st].append(idx)

        q = deque([[0, source]])
        visited = set([source])
        while q:
            dist, cur = q.popleft()
            for rti in adj[cur]:
                for st in routes[rti]:
                    if st not in visited:
                        if st == target:
                            return dist + 1
                        q.append((dist + 1, st))
                        visited.add(st)
                routes[rti] = []
        return -1