class Solution:
    def isHappy(self, n: int) -> bool:
        # Solution detecting cycles similar to linked list cycles
        
        def SumSquares(n):
            s = 0
            while n > 0:
                s += (n % 10) ** 2
                n //= 10
            return s
    
        slow, fast = n, SumSquares(n)

        while slow != fast:
            slow = SumSquares(slow)
            fast = SumSquares(fast)
            fast = SumSquares(fast)
        return fast == 1

    
    def isHappy2(self, n: int) -> bool:
        # Math solution
        
        while n > 9:
            s, d = 0, n
            while d > 0:
                s += pow(d % 10, 2)
                d //= 10
            n = s
        return n == 1 or n == 7