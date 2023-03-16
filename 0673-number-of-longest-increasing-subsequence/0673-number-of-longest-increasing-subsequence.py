class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        dp = {}
        lenLIS, res = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            maxLIS, maxCnt = 1, 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, cnt = dp[j]
                    if length + 1 > maxLIS:
                        maxLIS, maxCnt = length + 1, cnt
                    elif length + 1 == maxLIS:
                        maxCnt += cnt
            if maxLIS > lenLIS:
                lenLIS, res = maxLIS, maxCnt
            elif lenLIS == maxLIS:
                res += maxCnt
            dp[i] = [maxLIS, maxCnt]
        return res
                