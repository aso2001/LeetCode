class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        hh = []
        proj = [(cap, pft) for cap, pft in zip(capital, profits)]
        heapq.heapify(proj)
          
        cnt = 0
        while cnt < k:
            while proj and proj[0][0] <= w:
                cap, pft = heapq.heappop(proj)
                heapq.heappush(hh, -pft)
            if hh:
                w -= heapq.heappop(hh)
                cnt += 1
            else: 
                break
        return w