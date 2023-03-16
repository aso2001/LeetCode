class TimeMap:

    def __init__(self):
        self.dd = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dd:
            tmp = self.dd[key]
            tmp.append((timestamp, value))
            self.dd[key] = tmp
        else:
            self.dd[key] = [(timestamp, value)]
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dd:
            return ""
        tmp = self.dd[key]
        L, R, res = 0, len(tmp) - 1, ""
        while L <= R:
            mid = (L + R) // 2
            if timestamp < tmp[mid][0]:
                R = mid - 1
            elif timestamp >= tmp[mid][0]:
                res = tmp[mid][1]
                L = mid + 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)