class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = 0
        for c in s:
            if c == '1':
                cnt += 1
        return '0'*(len(s) - 1) + '1' if cnt == 1 else '1'*(cnt - 1) + '0'*(len(s) - cnt) + '1'