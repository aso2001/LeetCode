from sortedcontainers import SortedDict
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        diff = SortedDict({0: 0})
        for s, e in flowers:
            diff[s] = diff.get(s, 0) + 1
            diff[e + 1] = diff.get(e + 1, 0) - 1
        
        cur, pos, pfx = 0, [], []
        for key, val in diff.items():
            pos.append(key)
            cur += val
            pfx.append(cur)

        res = []
        for p in people:
            i = bisect_right(pos, p) - 1
            res.append(pfx[i])
        return res