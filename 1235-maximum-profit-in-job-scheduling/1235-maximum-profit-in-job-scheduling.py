class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        tmp = sorted(zip(startTime, endTime, profit))
        cache = {}

        def dfs(i):
            if i == len(profit):
                return 0
            if i in cache:
                return cache[i]

            res = dfs(i + 1)
            jp = bisect.bisect(tmp, (tmp[i][1], -1, -1))
            res = max(res, tmp[i][2] + dfs(jp))
            cache[i] = res
            return res

        res = 0
        return dfs(0)
    

    def jobScheduling2(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = [0]*len(startTime)
        tmp = []
        for i in range(len(startTime)):
            triple = (startTime[i], endTime[i], profit[i])
            tmp.append(triple)

        tmp = sorted(list(zip(endTime,startTime,profit)))
        sorted(tmp, key=lambda x: x[1])
        endTime = [i[0] for i in tmp]
        print(endTime)
        for i in range(len(startTime)):
            pi = bisect_right(endTime, tmp[i][1] )
            dp[i] = max(dp[i], dp[i - 1], tmp[i][2] + dp[pi - 1])
        
        return max(dp)