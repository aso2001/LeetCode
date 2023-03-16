class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums

    def reset(self) -> List[int]:
        return self.array

    def shuffle(self) -> List[int]:
        n = self.array[:]
        ln = len(n)

        #random.shuffle(n)

        for i in range(ln):
            j = random.randrange(0,ln)
            n[i], n[j] = n[j], n[i]
        return n


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()