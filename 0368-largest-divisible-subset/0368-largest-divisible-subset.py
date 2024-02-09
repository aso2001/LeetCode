class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = {}
        
        nums.sort()
        
        def dfs(i, prev):
            if i == len(nums):
                return []
            if (i, prev) in dp:
                return dp[(i, prev)]
            res = dfs(i + 1, prev)
            if not nums[i] % prev:
                tmp = [nums[i]] + dfs(i + 1, nums[i])
                res = tmp if len(tmp) > len(res) else res 
            dp[(i, prev)] = res
            return res
        
        return dfs(0, 1)