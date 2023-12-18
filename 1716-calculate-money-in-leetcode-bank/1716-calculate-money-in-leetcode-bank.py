class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        nw = n // 7
        for k in range(7):
            res += nw * (2 * (k + 1) + (nw - 1)) / 2
        nd = n % 7
        for i in range(1, nd + 1):
            res += nw + i
        return int(res)