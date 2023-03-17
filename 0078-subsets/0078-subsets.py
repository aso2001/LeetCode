class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Recursive solution
        res = []
        ss = []
        def rec(i):
            if i == len(nums):
                res.append(ss.copy())
                return res
            ss.append(nums[i])
            rec(i + 1)
            ss.pop()
            rec(i + 1)

        rec(0)
        return res