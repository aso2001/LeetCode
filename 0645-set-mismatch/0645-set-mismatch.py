class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dd, res = {}, []
        for nn in nums:
            if nn in dd:
                res.append(nn)
            else:
                dd[nn] = 1
        for i in range(1, len(nums) + 1):
            if i not in dd:
                res.append(i)
        return res