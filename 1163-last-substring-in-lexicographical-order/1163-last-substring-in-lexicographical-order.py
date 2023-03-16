class Solution:
    def lastSubstring(self, s: str) -> str:
        ls = len(s)

        prev = s
        prev_i = s[0]
        for i in range(1,ls):
            if s[i] >= prev_i and s[i:] > prev:
                prev = s[i:]
                prev_i = s[i]
        print(prev)
        return prev