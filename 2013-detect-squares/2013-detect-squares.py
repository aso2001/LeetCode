class DetectSquares:

    def __init__(self):
        self.dp = {}

    def add(self, point: List[int]) -> None:
        pp = tuple(point)
        if pp not in self.dp:
            self.dp[pp] = 1
        else:
            self.dp[pp] += 1

    def count(self, point: List[int]) -> int:
        x, y = set(), set()
        for d in self.dp.keys():
            if d[0] == point[0]:
                y.add(d[1])
            elif d[1] == point[1]:
                x.add(d[0])
        res = 0
        for xx in x:
            x1 = xx
            y1 = point[1] - abs(point[0] - xx)
            pp = (x1, y1)
            tmp = 1
            if y1 in y and pp in self.dp:
                tmp *= self.dp[pp]
                tt1 = (point[0], y1)
                tt2 = (x1, point[1])
                tmp *= self.dp[tt1]
                tmp *= self.dp[tt2]
                res += tmp

            y1 = point[1] + abs(point[0] - xx)
            pp = (x1, y1)
            tmp = 1
            if y1 in y and pp in self.dp:
                tmp *= self.dp[pp]
                tt1 = (point[0], y1)
                tt2 = (x1, point[1])
                tmp *= self.dp[tt1]
                tmp *= self.dp[tt2]
                res += tmp
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)