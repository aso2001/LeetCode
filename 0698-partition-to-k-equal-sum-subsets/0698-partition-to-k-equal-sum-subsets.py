class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        s = sum(nums)
        if s % k: return False
        s /= k

        nums.sort(reverse = True)
        t = [s]*k

        def backtrack(i):
            if i == len(nums):
                return True

            dp = set()
            for j in range(k):
                if nums[i] <= t[j] and t[j] not in dp:
                    t[j] -= nums[i]
                    if backtrack(i + 1):
                        return True
                    t[j] += nums[i]
                    dp.add(t[j])
            return False

        return backtrack(0)