class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        pushed = pushed[::-1]
        popped = popped[::-1]

        while pushed and popped:
            while pushed and popped and pushed[-1] != popped[-1]:
                stack.append(pushed.pop())
            if pushed and popped and pushed[-1] == popped[-1]:
                pushed.pop()
                popped.pop()
            while popped and stack and stack[-1] == popped[-1]:
                popped.pop()
                stack.pop()

        #print(pushed, popped, stack)
        if not pushed and popped:
            if stack != popped:
                return False
        return True