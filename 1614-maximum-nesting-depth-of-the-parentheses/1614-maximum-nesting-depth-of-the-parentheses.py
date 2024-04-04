class Solution:
    def maxDepth(self, s: str) -> int:
        stack, res = [], 0
        for i in range(len(s)):
            if s[i] != '(' and s[i] != ')':
                pass
            elif s[i] == '(':
                stack.append('(')
                res = max(res, len(stack))
            elif s[i] == ')':
                stack.pop()
        return res