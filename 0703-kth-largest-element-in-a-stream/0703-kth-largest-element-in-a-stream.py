class KthLargest:

    import heapq

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hh = nums
        heapq.heapify(self.hh)
        while len(self.hh) > k:
            heapq.heappop(self.hh)
        
    def add(self, val: int) -> int:
        if not self.hh or len(self.hh) < self.k:
            heapq.heappush(self.hh, val)   
        elif len(self.hh) == self.k:
            if self.hh[0] <= val:
                heapq.heappop(self.hh)
                heapq.heappush(self.hh, val)
        return self.hh[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)