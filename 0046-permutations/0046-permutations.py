class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        else:
            res = []
            perms = self.permute(nums[1:])
            for i in range(len(nums)):
                for p in perms:
                    tmp = list(p)
                    tmp.insert(i, nums[0])
                    res.append(tmp)
            return res