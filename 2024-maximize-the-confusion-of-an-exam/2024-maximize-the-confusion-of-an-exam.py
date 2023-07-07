class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        L, R, res, cnt = 0, -1, 0, 0
        while R < len(answerKey) - 1:
            if answerKey[R + 1] == 'F' and cnt < k:
                cnt += 1
                R += 1
            elif answerKey[R + 1] == 'T':
                R += 1
            else:
                while answerKey[L] != 'F':
                    L += 1
                R += 1
                L += 1
            res = max(res, R - L + 1)

        L, R, cnt = 0, -1, 0
        while R < len(answerKey) - 1:
            if answerKey[R + 1] == 'T' and cnt < k:
                cnt += 1
                R += 1
            elif answerKey[R + 1] == 'F':
                R += 1
            else:
                while answerKey[L] != 'T':
                    L += 1
                L += 1
                R += 1
            res = max(res, R - L + 1)
        return res