class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        res = []
        L = R = nums[0]
        i = 1
        while True:
            while i < len(nums) and nums[i] - nums[i-1] == 1:
                R = nums[i]
                i += 1
            if R == L:
                res.append(str(L))
            else:
                res.append(str(L) + "->" + str(R))
            if i >= len(nums) - 1:
                if i == len(nums)-1:
                    res.append(str(nums[i]))
                return res
            L = nums[i]
            R = nums[i]
            i += 1  