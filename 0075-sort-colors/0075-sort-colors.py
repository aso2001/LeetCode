class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 1 pass solution
        L, i, R = 0, 0, len(nums) - 1
        while i <= R:
            if nums[i] == 0:
                nums[L], nums[i] = nums[i], nums[L]
                L += 1
                i += 1
            elif nums[i] == 2:
                nums[R], nums[i] = nums[i], nums[R]
                R -= 1
            else:
                i += 1
          
        
    def sortColors2(self, nums: List[int]) -> None:
        # 2 pass solution using counters
        c0, c1, c2 = 0, 0, 0
        for n in nums:
            if n == 0: c0 += 1
            elif n == 1: c1 += 1
            else: c2 += 1
        for i in range(c0):
            nums[i] = 0
        for i in range(c1):
            nums[i + c0] = 1
        for i in range(c2):
            nums[i + c0 + c1] = 2