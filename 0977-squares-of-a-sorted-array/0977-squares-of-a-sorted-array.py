class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        L, R = 0, len(nums) - 1
        while L < R:
            if abs(nums[L]) < abs(nums[R]):
                res.append(nums[R] * nums[R])
                R -= 1
            else:
                res.append(nums[L] * nums[L])
                L += 1
        res.append(nums[L] * nums[L])
        return  res[::-1]