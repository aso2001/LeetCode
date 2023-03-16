class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if n == 1 else -1
        if n > len(trust) + 1: return -1
        pall = set()
        pt = set()
        cand = set()

        for t in trust:
            pall.add(t[0])
            pt.add(t[1])
        if len(pall) < n - 1:
            return -1
        for t in trust:
            if t[1] not in pall:
                cand.add(t[1])
        for c in cand:
            cnt = 0
            for a in pall:
                if [a, c] not in trust:
                    break
                cnt += 1
            if cnt == len(pall):
                return c
        return -1