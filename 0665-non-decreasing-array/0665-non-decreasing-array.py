class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        cnt = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
                cnt += 1
            if cnt > 1:
                return False
        return True