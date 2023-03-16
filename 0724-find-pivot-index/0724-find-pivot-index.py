class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum, rsum = 0, sum(nums) - nums[0]
        for i in range(0, len(nums) - 1):
            if lsum == rsum:
                return i
            lsum += nums[i]
            rsum -= nums[i + 1]
        if sum(nums) - nums[-1] == 0: return len(nums) - 1
        return -1