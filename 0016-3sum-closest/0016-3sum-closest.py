class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mx = -math.inf
        mn = math.inf
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                if (nums[L] + nums[R] + nums[i]) > target:
                    mn = min(mn, nums[L] + nums[R] + nums[i])
                    R -= 1
                elif (nums[L] + nums[R] + nums[i]) < target:
                    mx = max(mx, nums[L] + nums[R] + nums[i])
                    L += 1
                else:
                    return target
        return mn if (mn - target) < (target - mx) else mx