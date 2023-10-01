class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        w = ''
        for i in range(len(s)):
            if i == len(s) - 1:
                res.append(s[i])
                res.append(w[::-1])
            if s[i] == ' ':
                res.append(w[::-1])
                res.append(' ')
                w = ''
            else:
                w += s[i]
        return "".join(res)