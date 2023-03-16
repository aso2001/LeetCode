class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        num = num[::-1]
        kk = []
        while k > 9:
            kk.append(k % 10)
            k //= 10
        kk.append(k)

        if len(kk) > len(num):
            kk, num = num, kk
        res, carry = [], 0
        for i in range(len(num)):
            if len(kk) > i:
                ss = num[i] + kk[i] + carry
            else:
                ss = num[i] + carry
            res.append(ss % 10)
            carry = ss // 10
        if carry:
            res.append(1)

        return res[::-1]