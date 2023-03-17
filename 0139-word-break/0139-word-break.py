class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Bottom up DP solution O(n*m*n)  
        dp = [False]*(len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]

    
    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        # TLE
        dp = [False]*(len(s) + 1)
        d, lw = {}, []
        for w in wordDict:
            if len(w) not in lw: lw.append(len(w))
            d[w] = 1
        lw.sort()
        chk, i = [0], 0
        while chk:
            i = chk.pop()
            if i > len(s) - lw[0]:
                continue
            for j in lw:
                if i + j <= len(s):
                    if s[i:i + j] in d:
                        dp[i + j] = True
                        chk.append(i + j)
                else:
                    break
        return dp[len(s)]