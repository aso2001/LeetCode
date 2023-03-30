class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True

        dp = [[[False]*len(s1) for _ in range(len(s1))] for _ in range(len(s1) + 1)]

        for i in range(len(s1)):
            for j in range(len(s1)):
                dp[1][i][j] = (s1[i] == s2[j])

        for Len in range(2, len(s1) + 1):
            for i in range(len(s1) - Len + 1):
                for j in range(len(s1) - Len + 1):
                    for k in range(1, Len):
                        if (dp[k][i][j] and dp[Len - k][i + k][j + k]) or (dp[k][i][j + Len - k] and dp[Len - k][i + k][j]):
                            dp[Len][i][j] = True

        return dp[len(s1)][0][0]