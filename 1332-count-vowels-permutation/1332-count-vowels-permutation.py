class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7
        a = e = i = o = u = 1
        for j in range(2, n + 1):
            new_a = (e + u + i)%mod
            new_e = (a + i)%mod
            new_i = (e + o)%mod
            new_o = i%mod
            new_u = (o + i)%mod
            a, e, i, o, u = new_a, new_e, new_i, new_o, new_u
        res = (a + e + i + o + u)%mod
        return int(res)