class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        cnt = 0
        for i in range(len(nums)):
            if not nums[i] % 2:
                nums[i], nums[cnt] = nums[cnt], nums[i]
                cnt += 1
        return nums    