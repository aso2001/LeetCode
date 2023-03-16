class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.wdict = {}
        self.wdict[0] = [0, w[0]]
        prev = w[0]
        for i in range(1,len(w)):
            self.wdict[i] = [prev, prev + w[i]]
            prev += w[i]
        self.sum = prev

    def pickIndex(self) -> int:
        tmp = random.randrange(1, self.sum + 1)
        low = 0
        high = len(self.w) - 1
        mid = 0
        if high == 0:
            return 0
        while low <= high:
            mid = (low + high)//2
            tmp_d = self.wdict[mid]
            if tmp <= tmp_d[0]:
                high = mid - 1
            elif tmp > tmp_d[1]:
                low = mid + 1
            else:
                return mid

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()