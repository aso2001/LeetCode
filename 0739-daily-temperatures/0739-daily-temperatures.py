class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0]*len(t)
        stack = []
        for i in range(len(t)):
            while stack and stack[-1][0] < t[i]:
                top = stack.pop()
                res[top[1]] = i - top[1]
            stack.append((t[i], i))
        return res