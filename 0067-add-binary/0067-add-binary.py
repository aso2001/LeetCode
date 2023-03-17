class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res, extra = '', 0
        if len(a) < len(b):
            a, b = b, a
        a, b= a[::-1], b[::-1]

        for i in range(len(a)):
            if i < len(b):
                c = int(a[i]) + int(b[i]) + extra
            else:
                c = int(a[i]) + extra
            res += str(c%2)
            extra = c // 2
        if extra: res += '1'
        return res[::-1]

    
    def addBinary2(self, a: str, b: str) -> str:

        if len(a) < len(b):
            a, b = b, a
        res = [0]*(len(a) + 1)

        extra = 0
        j = len(b) - 1
        for i in range(len(a) - 1, -1, -1):
            if j >= 0:
                c = int(a[i]) + int(b[j]) + extra
                j -= 1
            else:
                c = int(a[i]) + extra
            res[i + 1] = str(c%2)
            extra = c // 2
        res[0] = str(extra)
        if res[0] == '0':
            res = res[1:]
        return ''.join(res)