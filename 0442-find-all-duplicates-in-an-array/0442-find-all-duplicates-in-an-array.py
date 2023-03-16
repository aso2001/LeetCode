class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Store info about visited index using negative sign
        res = []

        for n in nums:
            if nums[abs(n) - 1] < 0:
                res.append(abs(n))
            else:
                nums[abs(n) - 1] = -nums[abs(n) - 1]        
        return res
    

    def findDuplicates2(self, nums: List[int]) -> List[int]:

        res = []

        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                res.append(abs(nums[i]))
            else:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]        
        return res