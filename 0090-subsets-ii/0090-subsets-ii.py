class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Solution skipping duplicates in backracking 
        nums.sort()
        res = []

        def dfs(i, ds):
            res.append(ds.copy())
            if i == len(nums):
                return
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                ds.append(nums[j])
                dfs(j + 1, ds)
                ds.pop()
        dfs(0, [])
        return res
    

    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        # Solution using set() to eliminate duplicates in results
        nums.sort()

        res = set()
        def dfs(i, ds):
            if i == len(nums):
                res.add(tuple(ds))
                return
            dfs(i + 1, ds + [nums[i]])
            dfs(i + 1, ds)
        dfs(0, [])
        return res