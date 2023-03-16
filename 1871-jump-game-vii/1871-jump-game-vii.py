class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        q =deque([0])
        last = 0
        while q:
            i = q.popleft()
            if i == len(s) - 1:
                return True
            L = max(i + minJump, last + 1)
            R = min(i + maxJump, len(s) - 1)
            for j in range(L, R + 1):
                if s[j] == '0':
                    q.append(j)
            last = i + maxJump
        return False