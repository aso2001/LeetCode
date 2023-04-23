class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9 + 7
        
        @lru_cache(None)
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            res = 0
            for ii in range(i, len(s)):
                si = int(s[i:ii+1])
                if si <= k:
                    res += dfs(ii + 1)
                else:
                    break
            return res % mod
        return dfs(0)