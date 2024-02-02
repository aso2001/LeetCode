class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        s = '123456789'
        s1 = int(s)
        j = len(str(low))
        s0, i = 0, 0

        while s0 <= s1:
            s0 = int(s[i:i+j])
            res.append(s0)
            i += 1
            if j == 9:
                break
            if i + j > 9:
                i = 0
                j += 1

        i1, i2 = 0, 0
        for i in range(len(res)):
            if res[i] < low:
                i1 += 1
            if res[i] <= high:
                i2 = i
        if res[i2] > high:
            return []
        return res[i1:i2+1]