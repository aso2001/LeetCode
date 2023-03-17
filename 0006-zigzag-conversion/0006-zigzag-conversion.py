class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        nr, ci, (nc, lc) = numRows, 2*numRows - 2, divmod(len(s), 2*numRows - 2)
        if lc: nc += 1
        
        cnt, ll = 0, [""]*nr
        for j in range(nc):
            for i in range(2*nr - 2):
                if i < nr:
                    ll[i] += s[cnt]
                else:
                    ll[2*nr - 2 - i] += s[cnt]
                cnt += 1
                if cnt >= len(s):
                    break
        res = "".join(ll)
        return res

        # 1---9
        # 2--810
        # 3-7-11
        # 46--12
        # 5---13


    def convert2(self, s: str, numRows: int) -> str:

        nr = numRows
        if nr >= len(s) or nr == 1: return s

        i, nc, zig = 0, 0, 0
        while True:
            if not zig:
                if i + nr >= len(s):
                    nc += 1
                    break
                else:
                    i += nr
                    nc += 1
                    zig = 1
                    dv = nr - 1
            else:
                if dv:
                    if i + 1 <= len(s):
                        i += 1
                        nc += 1
                        dv -= 1
                    else:
                        break
                else:
                    zig = 0

        mx = [['']*nc for _ in range(nr)]

        zig, cnt, i, j = 0, 0, 0, 0
        while True:
            if cnt == len(s):
                break
            if not zig:
                mx[i][j] = s[cnt]
                cnt += 1
                if i == nr - 1:
                    i -= 1
                    j += 1
                    zig = 1
                else:
                    i += 1
            else:
                mx[i][j] = s[cnt]
                cnt += 1
                if i == 0:
                    i += 1
                    zig = 0
                else:
                    i -= 1
                    j += 1

        res = ""
        for i in range(nr):
            for j in range(nc):
                if mx != '':
                    res += mx[i][j]

        return res                                  