class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        prev, i, cnt = 0, 1, 1
        while i < len(nums):
            if nums[i] != nums[prev]:
                cnt += 1
                if i - prev > 1:
                    nums[prev + 1] = nums[i]
                    prev += 1
                else:
                    prev = i
            i += 1
        return cnt