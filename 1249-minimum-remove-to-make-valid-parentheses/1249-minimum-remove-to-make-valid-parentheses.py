class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res, cnt = "", 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0:
                    continue
                else:
                    cnt -= 1
            res = res + c
        res2, cnt = "", 0
        res2 = ""
        for c in res[::-1]:
            if c == ')':
                cnt += 1
            elif c == '(':
                if cnt == 0:
                    continue
                else:
                    cnt -= 1
            res2 = res2 + c
        return res2[::-1]