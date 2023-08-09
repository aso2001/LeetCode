class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        L, R = 0, nums[-1] - nums[0]

        def helper(guess):
            i, cnt = 1, 0
            while i < len(nums):
                if abs(nums[i] - nums[i-1]) <= guess:
                    cnt += 1
                    i += 2
                else:
                    i += 1 
            return cnt

        while L <= R:
            guess = (L + R) // 2
            res = helper(guess)
            if  res < p:
                L = guess + 1
            elif res >= p:
                R = guess - 1
        return L     