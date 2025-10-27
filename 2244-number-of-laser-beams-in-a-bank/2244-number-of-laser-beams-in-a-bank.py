class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        tmp, res = [], 0
        for i in range(len(bank)):
            cnt = 0
            for j in range(len(bank[0])):
                if bank[i][j] == '1':
                    cnt += 1
            if cnt:
                tmp.append(cnt)
        for i in range(1, len(tmp)):
            res += tmp[i - 1] * tmp[i]
        return res 