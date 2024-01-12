class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        a = s[:n]
        b = s[n:]
        cnt1, cnt2 = 0, 0
        for t in a:
            if t in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                cnt1 += 1
        for t in b:
            if t in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                cnt2 += 1
        return cnt1 == cnt2