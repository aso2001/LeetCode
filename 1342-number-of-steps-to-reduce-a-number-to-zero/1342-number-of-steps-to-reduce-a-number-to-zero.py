class Solution:
    def numberOfSteps(self, num: int) -> int:
        while num:
            if num%2 == 0: return 1 + self.numberOfSteps(num/2)
            else: return 1 + self.numberOfSteps(num-1)
        return 0