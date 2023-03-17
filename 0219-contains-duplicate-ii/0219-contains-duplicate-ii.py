class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        if len(nums) == 2 and len(set(nums))==1:
            return True
        for i in range(len(nums)-k):
            if len(set(nums[i:i+k+1]))<=k:
                return True
        return False