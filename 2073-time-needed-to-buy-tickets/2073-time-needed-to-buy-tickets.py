class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque(tickets)
        res = 0
        x = k
        while q[x] > 0:
            res += 1
            if q[0] == 1:
                if x == 0:
                    return res
                q.popleft()
                x -= 1
            else:
                tmp = q.popleft()
                q.append(tmp - 1)
                if x == 0:
                    x = len(q) - 1
                else:
                    x -= 1