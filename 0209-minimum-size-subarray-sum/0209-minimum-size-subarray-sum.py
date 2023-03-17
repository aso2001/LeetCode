class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        tsum, i = 0, 0
        # Find first subarray at the beginning and it's window (minw)
        while tsum < target and i < len(nums):
            tsum += nums[i]
            i += 1
        if tsum < target and i == len(nums): return 0
        minw = i
        i -= 1
        while target <= tsum - nums[i - minw + 1]:
            tsum -= nums[i - minw + 1]
            minw -= 1
        # Scan the rest of the array by reducing the window as needed
        while i < len(nums) - 1:
            i += 1
            tsum += (nums[i] - nums[i - minw])
            while target <= tsum - nums[i - minw + 1]:
                tsum -= nums[i - minw + 1]
                minw -= 1
        return minw