class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [nums[0]]*n
        pst = [nums[n-1]]*n
        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i] 
        for i in range(n-2,-1,-1):
            pst[i] = pst[i + 1] + nums[i]
        res = [0]*n
        for i in range(n):
            res[i] = nums[i]*i - (pre[i-1] if i > 0 else 0) + (pst[i+1] if i < n - 1 else 0) - nums[i]*(n - i - 1)
        return res