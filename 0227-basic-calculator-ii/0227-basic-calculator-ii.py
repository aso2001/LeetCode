class Solution:
    def calculate(self, s: str) -> int:

        res, cur, prev, i = 0, 0, 0, 0
        cur_oper = '+'

        while i < len(s):

            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = 10*cur + int(s[i])
                    i += 1
                i -= 1

                if cur_oper == '+':
                    res += cur
                    prev = cur
                elif cur_oper == '-':
                    res -= cur
                    prev = -cur
                elif cur_oper == '*':
                    res -= prev
                    res += prev * cur
                    prev = prev * cur
                elif cur_oper == '/':
                    res -= prev
                    res += int(prev/cur)
                    prev = int(prev/cur)
                cur = 0
        
            elif s[i] != ' ':
                cur_oper = s[i]
            i += 1            
        return res