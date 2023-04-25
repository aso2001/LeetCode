class SmallestInfiniteSet:

    def __init__(self):
        self.hh = []
        self.dd = {}
        for i in range(1, 1001):
            heappush(self.hh, i)
            self.dd[i] = 1
        
        
    def popSmallest(self) -> int:
        if self.hh:
            res = heappop(self.hh)
            del self.dd[res]
            return res


    def addBack(self, num: int) -> None:
        if num not in self.dd:
            self.dd[num] = 1
            heappush(self.hh, num)
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)