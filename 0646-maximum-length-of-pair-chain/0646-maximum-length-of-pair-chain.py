class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort()

        dp = [1]*len(pairs)
        for i in range(len(pairs) - 2, -1, -1):
            j = i + 1
            while j < len(pairs):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(1 + dp[j], dp[i])
                j += 1
        return max(dp)