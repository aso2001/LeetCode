class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        res = 0
        stack = []
        pfx = [0]
        for n in nums:
            pfx.append(pfx[-1] + n)

        for i in range(len(nums)):
            newStart = i
            while stack and stack[-1][1] > nums[i]:
                start, val = stack.pop()
                tot = pfx[i] - pfx[start]
                res = max(res, val * tot)
                newStart = start
            stack.append((newStart, nums[i]))

        for start, val in stack:
            tot = pfx[len(nums)] - pfx[start]
            res = max(res, val * tot)

        return res % (10**9 + 7)