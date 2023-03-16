class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        res = set()

        def backtrack(i):
            nonlocal res
            if i == len(nums) - 1:
                return res.copy()
            res1 = set()
            for r in res:
                if r[-1] <= nums[i + 1]:
                    tmp = list(r)
                    tmp.append(nums[i+1])
                    res1.add((*tmp,))
            res |= res1

        for i in range(len(nums)):
            ll = [nums[i]]
            res.add((*ll,))
            backtrack(i)

        res1 = res.copy()
        for rr in res:
            if len(rr) == 1:
                res1.remove(rr)
        return res1