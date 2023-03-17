class Solution:
    def myAtoi(self, s: str) -> int:

        if s == "": return 0
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s): return 0
        s = s[i:]
        if s == "": return 0
        sign = +1
        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign = -1
            s = s[1:]
            if s == "": return 0

        if s[0].isdigit():
            res, i = 0, 0
            while i < len(s) and s[i].isdigit() and res < 2147483648:
                res = 10*res + int(s[i])
                i += 1
            if res >= 2147483648 and sign == -1:
                return -2147483648
            elif res >= 2147483647 and sign == +1:
                return 2147483647
            else:
                return sign*res
        else:
            return 0