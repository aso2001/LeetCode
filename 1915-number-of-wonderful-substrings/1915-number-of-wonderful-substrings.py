class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        dd = {}
        dd[0] = 1

        mask = 0
        res = 0
        for c in word:
            bit = ord(c) - 97
            mask ^= (1 << bit)
            if mask in dd:
                res += dd[mask]
                dd[mask] += 1
            else:
                dd[mask] = 1

            for odd_c in range(0, 10):
                if (mask ^ (1 << odd_c)) in dd:
                    res += dd[mask ^ (1 << odd_c)]
        return res