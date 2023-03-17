class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True

        k = (bin(n)[2:])[::-1]

        flag = 0
        for i in range(len(k)):
            if k[i] == '1' and flag == 0:
                flag = 1
                if i%2 != 0:
                    return False
                continue
            if k[i] == '1' and flag == 1:
                return False

        return True