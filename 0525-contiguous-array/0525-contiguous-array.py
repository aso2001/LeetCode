class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pfx = [0]*len(nums)
        pfx[0] = -1 if not nums[0] else 1
        for i in range(1, len(nums)):
            pfx[i] = pfx[i - 1] - 1 if not nums[i] else pfx[i - 1] + 1
        dd = defaultdict(int)
        res = 0
        for i in range(len(nums)):
            if not pfx[i]:
                res = max(res, i + 1)
            if pfx[i] in dd:
                res = max(res, i - dd[pfx[i]])
            else:
                dd[pfx[i]] = i
        return res