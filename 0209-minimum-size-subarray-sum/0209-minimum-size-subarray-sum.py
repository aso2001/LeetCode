class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, R, res, ss = 0, 0, len(nums) + 1, nums[0]
        while R <= len(nums) - 1:
            if ss < target:
                if R < len(nums) - 1:
                    R += 1
                    ss += nums[R]
            else:
                res = min(res, R - L + 1)
                ss -= nums[L]
                L += 1
            if R == len(nums) - 1 and ss < target:
                break
        return res if res < len(nums) + 1 else 0

    def minSubArrayLen2(self, target: int, nums: List[int]) -> int:
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