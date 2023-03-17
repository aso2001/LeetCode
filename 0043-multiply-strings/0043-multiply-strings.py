class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        num1, num2, res = num1[::-1], num2[::-1], [0]*(len(num1) + len(num2))

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                dig = (ord(num1[i1]) - ord('0'))*(ord(num2[i2]) - ord('0'))
                res[i1 + i2] += dig
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10       
                       
        while res[-1] == 0: res.pop()
        res = ''.join(str(n) for n in res[::-1])
        return res