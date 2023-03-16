class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        xx = x ^ y
        setBits = 0
 
        while xx > 0 :
            setBits += xx & 1
            xx >>= 1
        return setBits