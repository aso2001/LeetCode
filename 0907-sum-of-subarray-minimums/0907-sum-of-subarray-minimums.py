class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        res = 0
        stack = []
        for i in range(len(arr)):
            while stack and arr[i] < stack[-1][1]:
                pair = stack.pop()
                left = pair[0] - stack[-1][0] if stack else pair[0] + 1
                right = i - pair[0]
                res = (res + pair[1] * left * right) % mod
            cur = (i, arr[i])
            stack.append(cur)

        for i in range(len(stack)):
            pair = stack[i]
            left = pair[0] - stack[i - 1][0] if i > 0 else pair[0] + 1
            right = len(arr) - pair[0]
            res = (res + pair[1] * left * right) % mod
        return res