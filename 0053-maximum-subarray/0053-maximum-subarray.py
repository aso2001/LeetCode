class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n, ln = nums, len(nums)

        if ln == 1:
            return n[0]

        ss = 0
        res = -10**5
        for i in range(ln):
            ss = max(n[i], ss + n[i])
            res = max(res, ss)
        return res
