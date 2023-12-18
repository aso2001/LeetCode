class Solution:
    def minTaps2(self, n: int, ranges: List[int]) -> int:
        rr = []
        for i in range(n + 1):
            if i - ranges[i] < 0:
                L = 0
            else:
                L = i - ranges[i]
            if i + ranges[i] > n:
                R = n
            else:
                R = i + ranges[i]
            pair = (L, R)
            rr.append(pair)
        rr.sort()
        print(rr)

        def check(a, b):
            L1, R1 = a
            L2, R2 = b
            if L2 <= R1:
                return True
            else:
                return False

        res = []
        i = 0
        i0 = -1
        tmp = (-1, -1)
        while i < n + 1 and rr[i][0] == 0:
            if rr[i][0] != rr[i][1]:
                tmp = rr[i]
                i0 = i
            i += 1
        if tmp[0] == 0:
            res.append(tmp)
        if tmp[1] == n: return 1
        if (i0 == n and tmp[1] < n) or i0 == -1: return -1
        tmp2 = (-1, -1)
        for i in range(i0 + 1, n + 1):
            if check(tmp, rr[i]):
                if tmp[1] < rr[i][1]:
                    tmp2 = rr[i]
                else:
                    continue
            else:
                if tmp2[0] == -1:
                    return -1
                else:
                    res.append(tmp2)
                    if tmp2[1] == n:
                        return len(res)
                    tmp = tmp2
                    tmp2 = (-1, -1)
        if tmp2[0] != -1 and tmp2[1] == n:
            return len(res) + 1


    def minTaps(self, n: int, ranges: List[int]) -> int:
        mx_reach = [0]*(n + 1)

        for i in range(len(ranges)):
            L = max(0, i - ranges[i])
            R = min(n, i + ranges[i])
            mx_reach[L] = max(mx_reach[L], R)
        
        res = 0
        cur_R = 0
        nxt_R = 0
        for i in range(n + 1):
            if i > nxt_R:
                return -1
            if i > cur_R:
                res += 1
                cur_R = nxt_R
            nxt_R = max(nxt_R, mx_reach[i])
        return res