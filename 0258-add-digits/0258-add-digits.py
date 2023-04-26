class Solution:
    def addDigits2(self, num: int) -> int:
        while num > 9:
            tmp = 0
            tmp += num % 10
            num //= 10
            num += tmp
        return num
    
    # Math solution
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9