class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        def log2(x, base):
            return int(log(x) / log(base))

        res = 0
        for i in nums:
            res = res ^ i
        # find the position of the rightmost set bit in `res`
        k = log2(res & -res, 2)
        # `x` and `y` are two odd appearing elements
        x = y = 0
        
        for i in nums:
            # elements that have k'th bit set
            if i & (1 << k):
                x = x ^ i
            # elements that don't have k'th bit set
            else:
                y = y ^ i
        return x, y 
        