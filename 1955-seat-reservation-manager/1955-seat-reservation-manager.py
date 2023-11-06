class SeatManager:

    def __init__(self, n: int):
        self.hh = list(range(1, n+1))
        heapq.heapify(self.hh)
        
    def reserve(self) -> int:
        return heapq.heappop(self.hh)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.hh, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)