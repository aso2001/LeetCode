class MedianFinder:

    def __init__(self):
        self.hleft = []
        self.hright = []

    def addNum(self, num: int) -> None:
        if not len(self.hright):
            heapq.heappush(self.hright, num)
        elif num >= self.hright[0]:
            if len(self.hright) == len(self.hleft):
                heapq.heappush(self.hright, num)
            else:
                tmp = heapq.heappop(self.hright)
                heapq.heappush(self.hleft, -tmp)
                heapq.heappush(self.hright, num)
        elif num < self.hright[0]:
            if len(self.hright) - len(self.hleft) == 1:
                heapq.heappush(self.hleft, -num)
            else:
                tmp = heapq.heappop(self.hleft)
                heapq.heappush(self.hright, max(-tmp, num))
                heapq.heappush(self.hleft, max(tmp, -num))

    def findMedian(self) -> float:
        if len(self.hleft) == len(self.hright):
            return (self.hright[0] - self.hleft[0])/2.
        else:
            return self.hright[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# 1 2 3 4 -3 -2 |1 10   -3 -2 1 2 3 4

# L  R
# -1 2
# 2  3
# 3  4