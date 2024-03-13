class Solution:
    def pivotInteger(self, n: int) -> int:
        pfx = [1]*n
        for i in range(1, n):
            pfx[i] = (i + 1) * (i + 2) // 2
        for i in range(n):
            if pfx[i] == pfx[n - 1] - (0 if i == 0 else pfx[i - 1]):
                return i + 1
        return -1