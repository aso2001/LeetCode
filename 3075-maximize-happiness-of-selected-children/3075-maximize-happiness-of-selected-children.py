class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        hh = [-h for h in happiness]
        heapq.heapify(hh)
        
        res, turns = 0, 0

        for i in range(k):
            res += max(-heapq.heappop(hh) - turns, 0)
            turns += 1  
        return res