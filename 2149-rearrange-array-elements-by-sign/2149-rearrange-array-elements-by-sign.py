class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        for n in nums:
            if n > 0: pos.append(n)
            else: neg.append(n)
        i = 0
        for (p,n) in zip(pos, neg):
            nums[i], nums[i + 1], i = p, n, i + 2
        return nums