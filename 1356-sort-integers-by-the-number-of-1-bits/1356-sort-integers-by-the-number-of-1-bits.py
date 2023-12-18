class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        pp = []
        arr.sort()
        for a in arr:
            ab = str(bin(a))
            cnt = 0
            for s in ab:
                if s == '1':
                    cnt += 1
            pair = (a, cnt)
            pp.append(pair)
        pp.sort(key=lambda x: x[1])
        res = []
        for p in pp:
            res.append(p[0])
        return res