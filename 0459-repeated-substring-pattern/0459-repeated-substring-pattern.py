class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)):
            if 2*(i + 1) > len(s): break
            cpy = s[0:i + 1]
            j = i + 1
            while j + len(cpy) <= len(s):
                if cpy == s[j:j + len(cpy)]:
                    if j + len(cpy) >= len(s):
                        return True
                    j += len(cpy)
                else:
                    break
        return False