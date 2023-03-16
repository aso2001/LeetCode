class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:

        min_val = min_div = math.inf
        hmax = []
        for nn in nums:
            if nn%2:
                nn *= 2
            min_val = min(min_val, nn)
            hmax.append(-nn)
        heapq.heapify(hmax)
        
        while not hmax[0]%2:
            nh = int(heapq.heappop(hmax)/2)
            heapq.heappush(hmax, nh)
            min_val = min(min_val, -nh)
            min_div = min(min_div, -hmax[0] - min_val)     
        return min_div