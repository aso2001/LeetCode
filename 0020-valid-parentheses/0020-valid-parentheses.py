class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(',']':'[','}':'{'}
        stack = []
        for ss in s:
            if ss in ['(','[','{']:
                stack.append(ss)
            elif ss in d:
                if not stack or stack.pop() != d[ss]:
                    return False
        return True if not stack else False