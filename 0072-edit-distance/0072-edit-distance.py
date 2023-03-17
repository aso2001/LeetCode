class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # DP bottom-up solution
        dp = [[math.inf]*(len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j   

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return dp[0][0]

    
    def minDistance2(self, word1: str, word2: str) -> int:
        # Recursive solution with memoisation
        dp = [[math.inf]*len(word2) for _ in range(len(word1))]
        
        def dist(i, j):
            if j == len(word2) and i < len(word1):
                return len(word1) - i
            if i == len(word1) and j < len(word2):
                return len(word2) - j
            if i == len(word1) and j == len(word2):
                return 0
            if dp[i][j] != math.inf:
                return dp[i][j]
            if word1[i] == word2[j]:
                return dist(i + 1, j + 1)
            else:
                m1 = 1 + dist(i, j + 1)
                m2 = 1 + dist(i + 1, j)
                m3 = 1 + dist(i + 1, j + 1)
                dp[i][j] = min(m1, m2, m3)
                return dp[i][j]
        return dist(0, 0)