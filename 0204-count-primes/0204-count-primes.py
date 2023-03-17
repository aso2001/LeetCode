class Solution:
    def countPrimes(self, n: int) -> int:
        # Sieve of Eratosthenes Algorithm O(n*log(log(n))) time complexity
        if n <= 1: return 0
        prime = [True]*n
        prime[0], prime[1] = False, False
        for i in range(2, int(n**0.5) + 1):
            if prime[i]:
                for j in range(i*i, n, i):
                    prime[j] = False
        return sum(prime) 