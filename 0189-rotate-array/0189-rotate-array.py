class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if not k or k == len(nums): return
        if k > len(nums): k %= len(nums)
        
        for i in range(len(nums)//2):
            nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]
        for i in range(k//2):
            nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]
        for i in range(k, (len(nums) + k)//2):
            nums[i], nums[len(nums) - 1 - i + k] = nums[len(nums) - 1 - i + k], nums[i]

        # k = 3
        # 1 2 3 4 5 6 7 initial state
        # 7 6 5 4 3 2 1 reverse array
        # 5 6 7 1 2 3 4 reverse 7 to 5 and 4 to 1 to get final result