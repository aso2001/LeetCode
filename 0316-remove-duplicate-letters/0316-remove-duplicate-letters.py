class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set() 
        last_occ = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in visited:
                while stack and c < stack[-1] and i < last_occ[stack[-1]]:
                    visited.discard(stack.pop())
                visited.add(c)
                stack.append(c)
        return ''.join(stack)