class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        dp = []
        dp2 = [math.inf] * (n + 1)

        for i in range(n):
            idx = bisect.bisect(dp2, obstacles[i])
            dp.append(idx + 1)
            dp2[idx] = obstacles[i]
        return dp
    
    def longestObstacleCourseAtEachPosition2(self, obstacles: List[int]) -> List[int]:
        # TLE solution 
        dp = [1]*len(obstacles)

        for i in range(1, len(obstacles)):
            for j in range(i - 1, -1, -1):
                if obstacles[i] >= obstacles[j]:
                    dp[i] = max(dp[i], dp[j] + 1)   
        return dp