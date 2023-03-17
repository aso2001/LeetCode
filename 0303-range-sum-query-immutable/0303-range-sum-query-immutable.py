class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums.copy()
        self.d = [0]*(len(self.array) + 1)
        self.d[0] = 0
        tmp = 0
        for i in range(1, len(nums) + 1):
            tmp += self.array[i - 1]
            self.d[i] = tmp

    def sumRange(self, left: int, right: int) -> int:
        return self.d[right + 1] - self.d[left]
    

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)