class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1
        for i in range(2, len(num)):
            if num[i - 2] == num[i - 1] and num[i - 1] == num[i]:
                res = max(res, int(num[i]))
        return '' if res == -1 else str(res) + str(res) + str(res)