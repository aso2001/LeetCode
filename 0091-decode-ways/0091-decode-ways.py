class Solution:
    def numDecodings(self, s: str) -> int:
        # DP solution
        if s[0] == "0": return 0
        dp = [0]*(len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if i < len(s) - 1 and ((s[i] == "2" and s[i+1] in "0123456") or s[i] == "1"):
                dp[i] += dp[i + 2]
        return dp[0]
    
    
    def numDecodings2(self, s: str) -> int:
        # Recursive solution
        def dfs(i, mem):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in mem:
                return mem[i]

            res = 0
            res += dfs(i + 1, mem)
            if i < len(s) - 1 and ((s[i] == "2" and s[i+1] in "0123456") or s[i] == "1"):
                res += dfs(i + 2, mem)
            mem[i] = res 
            return mem[i]

        mem = [None]*len(s)
        return dfs(0, mem)