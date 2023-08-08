class DetectSquares:
    def __init__(self):
        self.dp = defaultdict(int)
        self.pt = []

    def add(self, point: List[int]) -> None:
        pp = tuple(point)
        self.dp[pp] += 1
        self.pt.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        for x, y in self.pt:
            if abs(point[1] - y) == abs(point[0] - x) and x != point[0] and y != point[1]:
                res += self.dp[(x, point[1])] * self.dp[(point[0], y)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)