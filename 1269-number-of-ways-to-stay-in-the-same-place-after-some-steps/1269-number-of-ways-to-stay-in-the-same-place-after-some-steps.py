class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def dp(cur, rem):
            if rem == 0:
                if cur == 0:
                    return 1
                return 0
            res = dp(cur, rem - 1)
            if cur > 0:
                res = (res + dp(cur - 1, rem - 1))%mod
            if cur < arrLen - 1:
                res = (res + dp(cur + 1, rem - 1))%mod
            return res
        mod = 10 ** 9 + 7
        return dp(0, steps)