class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1: return 2

        def helper(i, j):
            nonlocal m
            chars[m] = chars[i]
            m += 1
            if 1 < j - i < 10:
                chars[m] = str(j - i)
                m += 1
            elif j - i >= 10:
                k = str(j - i)
                for ch in k:
                    chars[m] = ch
                    m += 1

        i, j, m = 0, 1, 0
        while j < len(chars):
            if chars[j] == chars[i]:
                j += 1
            else:
                helper(i, j)
                i = j
                j += 1
        helper(i, j)
        return m