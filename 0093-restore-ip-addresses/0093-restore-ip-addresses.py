class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []

        def backtrack(i, seq, cnt):
            if i == len(s) and cnt == 4:
                res.append(seq[:-1])
                return
            if cnt > 4:
                return

            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j + 1]) <= 255 and (i == j or s[i] != '0'):
                    backtrack(j + 1, seq + s[i:j + 1] + '.', cnt + 1)

        backtrack(0, '', 0)
        return res