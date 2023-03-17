class Solution:
    def strStr(self, h: str, n: str) -> int:
        if len(h) < len(n): return -1
        for i in range(len(h) - len(n) + 1):
            for j in range(len(n)):
                if n[j] != h[i + j]:
                    break
                if j == len(n) - 1:
                    return i
        return -1