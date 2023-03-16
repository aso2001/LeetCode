class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        sn = sorted(list(set(nums)))
        dd = {}
        for n in nums:
            if n in dd: dd[n] += 1
            else: dd[n] = 1

        dp = [0]*len(dd)
        dp[0] = dd[nums[0]] * nums[0]
        for i in range(1, len(dd)):
            if sn[i] != sn[i - 1] + 1:
                dp[i] = dd[sn[i]] * sn[i] + dp[i - 1]
            else:
                if i > 1:
                    dp[i] = max(dd[sn[i]] * sn[i] + dp[i - 2], dp[i - 1])
                else:
                    dp[i] = max(dd[sn[i]] * sn[i], dp[i - 1])
        return dp[len(dd) - 1]