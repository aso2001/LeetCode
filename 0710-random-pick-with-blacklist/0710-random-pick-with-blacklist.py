class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.dict = {}
        self.length = n - len(blacklist)
        j = n - 1
        for bl in blacklist:
            if bl < n - len(blacklist):
                while j in blacklist:
                    j -= 1
                self.dict[bl] = j
                j -= 1

    def pick(self) -> int:
        rnd = random.randrange(self.length)
        return self.dict.get(rnd,rnd)   # 2nd option to return rnd if not in dictionary for white listed numbers