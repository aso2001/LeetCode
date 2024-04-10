class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq = range(0, len(deck))
        dq = deque(dq)
        idx = []
        while dq:
            idx.append(dq.popleft())
            if dq:
                tmp = dq.popleft()
                dq.append(tmp)
        dd = dict(zip(idx, deck))
        res = [0]*len(deck)
        for i in range(len(deck)):
            res[i] = dd[i]
        return res