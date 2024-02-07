class Solution:
    def frequencySort(self, s: str) -> str:
        dd = defaultdict(int)
        res = ''
        for c in s:
            dd[c] += 1
        for k in sorted(dd, key=dd.get, reverse=True):
            res += k*dd[k]
        return res

    def frequencySort2(self, s: str) -> str:    
        res = ''
        dd = {c:s.count(c) for c in s}
        sorted(dd.items(), key = lambda x: x[1], reverse = False)
        sorted_count = dict(sorted(c.items(), key=lambda item: -item[1]))
        for key in dd:
            res += key*dd[key]
        return res[::-1]
        print(dd)
        # hh, res = [], ''
        # for d in dd:
        #     hh.append((-dd[d],d))
        # heapq.heapify(hh)
        # while hh:
        #     cnt, c = heapq.heappop(hh)
        #     res = res + c * (-cnt)
        #     res = ''.join(c * (-cnt))
        # return res