class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ')':
                stack.append(c)
            else:
                tmp = []
                while stack[-1] != '(':
                    tmp.append(stack.pop())
                stack.pop()
                stack.extend(tmp)
        return ''.join(stack)