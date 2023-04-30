class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        dd = set(strs)
        res, visited = 0, set()
        for ss in dd:
            if ss in visited:
                continue
            res += 1
            q = deque([ss])
            visited.add(ss)
            while q:
                for _ in range(len(q)):
                    s = q.popleft()
                    for nxt in dd:
                        if nxt != s and nxt not in visited:
                            d = sum([s[i] != nxt[i] for i in range(len(s))])
                            if d == 2:
                                q.append(nxt)
                                visited.add(nxt)
        return res