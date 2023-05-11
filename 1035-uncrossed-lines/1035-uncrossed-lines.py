class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[-1]*len(nums2) for _ in range(len(nums1))]

        def dfs(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0
            elif dp[i][j] != -1:
                return dp[i][j]
            elif nums1[i] == nums2[j]:
                dp[i][j] = 1 + dfs(i + 1, j + 1)
            else:
                dp[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))
            return dp[i][j]

        return dfs(0, 0)