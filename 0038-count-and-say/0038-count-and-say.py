class Solution:
    def countAndSay(self, n: int) -> str:
        prev = '1'
        for _ in range(1, n):
            new, cnt = "", 1
            for i in range(len(prev)):
                if i == len(prev) - 1:
                    new += str(cnt) + prev[i]
                elif prev[i] == prev[i+1]:
                    cnt += 1
                else:
                    new += str(cnt) + prev[i]
                    cnt = 1
            prev = new
        return prev