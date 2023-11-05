class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        q = deque(arr)
        winner = q.popleft()
        cnt = k 
        if k >= len(arr):
            return max(arr)
        while k:
            two = q.popleft()
            if winner > two:
                k -= 1
                q.append(two)
            else:
                k = cnt
                k -= 1
                q.append(winner)
                winner = two
        return winner