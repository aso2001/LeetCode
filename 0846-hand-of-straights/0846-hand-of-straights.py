class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand)%groupSize: return False

        dd = {}
        for h in hand:
            if h in dd: dd[h] += 1
            else: dd[h] = 1

        minH = list(dd.keys())
        heapq.heapify(minH)
        while minH:
            start = minH[0]
            for i in range(start, start + groupSize):
                if i not in dd:
                    return False
                dd[i] -= 1
                if dd[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True