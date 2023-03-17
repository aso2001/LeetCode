class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        dd = Counter(nums)

        res, perm = [], []

        def backtrack(i):
            if i == len(nums):
                res.append(perm.copy())
                return
            for d in dd:
                if dd[d] > 0:
                    perm.append(d)
                    dd[d] -= 1
                    backtrack(i + 1)
                    perm.pop()
                    dd[d] += 1

        backtrack(0)
        return res