class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res, cnt = 0, 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                cnt += 1
            res += cnt
        return res