class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        p = []
        for i in range(len(ages)):
            pair = (ages[i], scores[i])
            p.append(pair)
        p.sort()

        dp = [0]*len(p)
        res = 0
        for i in range(len(p)):
            dp[i] = p[i][1]
            res = max(res, dp[i])

        for i in range(len(p)):
            for j in range(i - 1, -1, -1):
                if p[i][1] >= p[j][1]:
                    dp[i] = max(dp[i], p[i][1] + dp[j])
            res = max(res, dp[i])
        return res 