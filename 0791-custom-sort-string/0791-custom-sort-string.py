class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = 0
        dd = {}
        for c in order:
            dd[c] = cnt
            cnt += 1
        ss = []
        for c in s:
            if c in dd:
                pair = (dd[c],c)
                ss.append(pair)
            else:
                pair = (27,c)
                ss.append(pair)
        ss.sort()
        res = ''
        for p in ss:
            res += p[1]
        return res