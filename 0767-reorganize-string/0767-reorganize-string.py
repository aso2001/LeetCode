class Solution:
    def reorganizeString(self, s: str) -> str:

        dd = {c: s.count(c) for c in s}
        hh = []
        for d in dd:
            hh.append((-dd[d], d))
        heapq.heapify(hh)

        res = []
        prev = None
        while hh:
            cnt, c = heapq.heappop(hh)
            if prev:
                heapq.heappush(hh, prev)
            res.append(c)
            if cnt < -1:
                prev = (cnt + 1, c)
            else:
                prev = None
        if prev:
            return ''
        return ''.join(res)