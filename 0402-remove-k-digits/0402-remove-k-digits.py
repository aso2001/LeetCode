class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num: return ""
        stack = [num[0]]
        for i in range(1, len(num)):
            while stack and stack[-1] > num[i] and k:
                stack.pop()
                k -= 1
            stack.append(num[i])
        while k:
            stack.pop()
            k -= 1
        res = "".join(stack).lstrip("0")
        return res if res != "" else "0"