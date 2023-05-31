class UndergroundSystem:

    def __init__(self):
        self.dd1 = defaultdict(list)
        self.dd2 = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dd1[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        (startStation, t0) = self.dd1[id]
        if (startStation, stationName) in self.dd2:
            (ot, nt) = self.dd2[(startStation, stationName)]
            self.dd2[(startStation, stationName)] = (ot + t - t0, nt + 1)
        else:
            self.dd2[(startStation, stationName)] = (t - t0,1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        (ot, nt) = self.dd2[(startStation, endStation)]
        return ot/nt        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)