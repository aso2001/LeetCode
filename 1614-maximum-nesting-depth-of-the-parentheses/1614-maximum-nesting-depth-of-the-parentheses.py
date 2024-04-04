class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        i, res = 0, 0
        while i < len(s):
            if s[i] != '(' and s[i] != ')':
                pass
            elif s[i] == '(':
                stack.append('(')
                res = max(res, len(stack))
            elif s[i] == ')':
                stack.pop()
            i += 1
        return res