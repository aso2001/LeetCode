class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                cnt = math.ceil(nums[i] / nums[i + 1])
                nums[i] //= cnt
                res += cnt - 1
        return res