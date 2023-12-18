class Solution:
    def sortVowels(self, s: str) -> str:
        owels = {'A','a','E','e','I','i','O','o','U','u'}
        s2 = []
        for c in s:
            if c in owels:
                s2.append(c)
        s2.sort()
        res, i = [], 0
        for c in s:
            if c in owels:
                res.append(s2[i])
                i += 1
            else:
                res.append(c)
        return ''.join(res)