class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        dd = {}
        for n in nums:
            nrev = int(str(n)[::-1])
            if n - nrev in dd:
                dd[n - nrev] += 1
            else:
                dd[n - nrev] = 1
        res = 0
        for d in dd:
            if dd[d] > 1:
                res += dd[d] * (dd[d] - 1) // 2
        return res % mod