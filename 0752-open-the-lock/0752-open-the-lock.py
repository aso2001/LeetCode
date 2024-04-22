class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = (0, 0, 0, 0)
        target = (int(target[0]), int(target[1]), int(target[2]), int(target[3]))
        deadends_i = []

        for d in deadends:
            dd = (int(d[0]), int(d[1]), int(d[2]), int(d[3]))
            deadends_i.append(dd)
        
        if start in deadends_i:
            return -1

        moves = [(-1, 0, 0, 0), (0, -1, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1), (1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]

        visited = set()
        q = deque([(start, 0)])
        while q:
            cur, lev = q.popleft()
            if cur == target:
                return lev
            for m in moves:
                nei = [0]*4
                for k in range(4):
                    if 0 <= cur[k] + m[k] <= 9:
                        nei[k] = cur[k] + m[k]
                    elif cur[k] + m[k] == 10:
                        nei[k] = 0
                    elif cur[k] + m[k] == -1:
                        nei[k] = 9
                if tuple(nei) not in deadends_i and tuple(nei) not in visited:
                    visited.add(tuple(nei))
                    q.append((tuple(nei), lev+1))
        return -1