class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res

        # 4^0 = 0^4 = 4, 1^1^2^2 = 1^2^1^2 = 0  ==>  1^2^4^1^2 = 4 XOR operator '^' is commutative a^b = b^a and a^0 = 0^a = a