class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS solution O(n) time, O(1) space
        L, R, maxR, cnt = 0, 0, 0, 0
        while R < len(nums) - 1:
            for i in range(L, R + 1):
                maxR = max(maxR, i + nums[i])
            L = R + 1
            R = maxR
            cnt += 1
        return cnt

    
    def jump2(self, nums: List[int]) -> int:
        # O(n^2) time solution
        dp = [len(nums)]*len(nums)
        dp[0] = 0
        for i in range(0, len(nums)):
            cnt = dp[i] + 1
            for j in range(1, nums[i] + 1):
                if i + j > len(nums) - 1:
                    return dp[len(nums) - 1]
                dp[i + j] = min(cnt, dp[i + j])
        return dp[len(nums) - 1]