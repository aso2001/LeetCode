class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1]*len(nums)
        if 2*k >= len(nums): return res
        ss = sum(nums[0:2*k+1])
        res[k] = ss//(2*k+1)
        L = 0
        R = L + 2*k + 1
        kk = k + 1
        while R < len(nums):
            ss += (-nums[L] + nums[R])
            res[kk] = ss//(2*k+1)
            kk += 1
            L += 1
            R += 1
        return res