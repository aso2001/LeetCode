class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        dd1, dd2 = {}, {}

        cur, cnt = node1, 0
        while cur != -1:
            if cur in dd1:
                break
            dd1[cur] = cnt
            cur = edges[cur]
            cnt += 1

        cur, cnt = node2, 0
        while cur != -1:
            if cur in dd2:
                break
            dd2[cur] = cnt
            cur = edges[cur]
            cnt += 1

        cand = set(dd1) & set(dd2)

        if not cand: return -1

        mdist, minc = math.inf, math.inf
        for c in cand:
            if max(dd1[c], dd2[c]) < mdist:
                mdist = max(dd1[c], dd2[c])
                minc = c
            elif max(dd1[c], dd2[c]) == mdist:
                minc = min(c, minc)
        return minc