class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        tot_len = 0
        for c in s:
            if c.isdigit():
                tot_len *= int(c)
            else:
                tot_len += 1
        for c in reversed(s):
            k %= tot_len 
            if not k and c.isalpha():
                return c
            if c.isdigit():
                tot_len //= int(c)
            else:
                tot_len -= 1
        return ""