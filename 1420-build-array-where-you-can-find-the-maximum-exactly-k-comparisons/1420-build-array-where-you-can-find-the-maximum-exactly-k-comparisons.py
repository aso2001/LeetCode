class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dp(i, cur_mx, left):
            if i == n:
                if left == 0:
                    return 1   
                return 0
            
            res = (cur_mx * dp(i + 1, cur_mx, left)) % MOD
            for num in range(cur_mx + 1, m + 1):
                res = (res + dp(i + 1, num, left - 1)) % MOD
            return res
        return dp(0, 0, k)         