class SummaryRanges:

    def __init__(self):
        self.intervals = None

    def addNum(self, value: int) -> None:

        def binary(L, R):
            while L < R:
                mid = (L + R)//2
                if value < self.intervals[mid][0]:
                    if value < self.intervals[mid - 1][1]:  # ?? out of range
                        return binary(L, mid - 1)
                    else:
                        if value == self.intervals[mid - 1][1]:
                            return
                        elif value == self.intervals[mid][0] - 1:
                            self.intervals[mid][0] -= 1
                            if value == self.intervals[mid - 1][1] + 1:
                                tmp = self.intervals[mid - 1][0]
                                self.intervals.pop(mid - 1)
                                self.intervals[mid - 1][0] = tmp
                            return
                        elif value == self.intervals[mid - 1][1] + 1:
                            self.intervals[mid - 1][1] += 1
                            if value == self.intervals[mid][0] - 1:
                                tmp = self.intervals[mid][1]
                                self.intervals.pop(mid)
                                self.intervals[mid - 1][1] = tmp
                            return
                        else:
                            self.intervals.insert(mid, [value, value])
                            return
                elif value > self.intervals[mid][1]:
                    if value > self.intervals[mid + 1][0]:
                        return binary(mid + 1, R)
                    else:
                        if value == self.intervals[mid + 1][0]:
                            return
                        elif value == self.intervals[mid + 1][0] - 1:
                            self.intervals[mid + 1][0] -= 1
                            if value == self.intervals[mid][1] + 1:
                                tmp = self.intervals[mid][0]
                                self.intervals.pop(mid)
                                self.intervals[mid][0] = tmp
                            return
                        elif value == self.intervals[mid][1] + 1:
                            self.intervals[mid][1] += 1
                            if value == self.intervals[mid + 1][0] - 1:
                                tmp = self.intervals[mid + 1][1]
                                self.intervals.pop(mid + 1)
                                self.intervals[mid][1] = tmp
                            return
                        else:
                            self.intervals.insert(mid + 1, [value, value])
                            return
                else: # value in the mid interval
                    return
            if self.intervals[L][0] <= value <= self.intervals[L][1]:
                return
            elif value < self.intervals[L][0] - 1:
                self.intervals.insert(L, [value, value])
                return
            elif value > self.intervals[L][1] + 1:
                self.intervals.insert(L + 1, [value, value])
                return
            elif value == self.intervals[L][0] - 1:
                self.intervals[L][0] -= 1
                if L - 1 >= 0 and value == self.intervals[L - 1][1] + 1:
                    tmp = self.intervals[L - 1][0]
                    self.intervals.pop(L - 1)
                    self.intervals[L - 1][0] = tmp
                return
            elif value == self.intervals[L][1] + 1:
                self.intervals[L][1] += 1
                if L + 1 < len(self.intervals) and value == self.intervals[L + 1][0] + 1:
                    tmp = self.intervals[L + 1][1]
                    self.intervals.pop(L + 1)
                    self.intervals[L][1] = tmp
                return

        if not self.intervals:
            self.intervals = []
            self.intervals.append([value, value])
        else:
            return binary(0, len(self.intervals) - 1)

    def getIntervals(self) -> List[List[int]]:
        return self.intervals        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()