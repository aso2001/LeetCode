class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        pre = [0]*(n+1)
        pst = [0]*(n+1)
        res = [0]*(n+1)
        print(pst[n-1])
        for i in range(1, n+1):
            pre[i] = pre[i - 1] + (0 if customers[i - 1] == 'Y' else 1)
        for i in range(n, 0, -1):
            pst[i-1] = pst[i] + (0 if customers[i-1] == 'N' else 1)
        for i in range(n+1):
            res[i] = pre[i] + pst[i]
        return res.index(min(res))