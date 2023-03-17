class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x = str(x)
        if len(x) == 1: return True        

        for i in range(int(len(x)//2)) :
            if x[i] != x[len(x) - 1 - i]:
                return False
        return True