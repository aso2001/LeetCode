class Solution:
    def myPow(self, x: float, n: int) -> float:

        def binExp(x, n):
            res = 1
            if n == 0:
                return res

            if n < 0:
                n = -1 * n
                x = 1.0 / x
                
            while n:
                if n % 2 == 1:
                    res *= x
                    n -= 1
                x *= x
                n //= 2
            return res

        return binExp(x, n)