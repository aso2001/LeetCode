class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        pref = [0]*len(cardPoints)
        post = [0]*len(cardPoints)

        s = 0
        e = 0
        for i in range(len(cardPoints)):
            s += cardPoints[i]
            e += cardPoints[len(cardPoints) - 1 - i]
            pref[i] = s
            post[len(cardPoints) - 1 - i] = e
        
        mxs = max(pref[k - 1], post[len(cardPoints) - k])
        for i in range(k - 1):
            mxs = max(mxs, pref[i] + post[len(cardPoints) - (k - i - 1)])
        return mxs

        # 1  3  20 1  2  40 9  8  7  2
        # 1  4  24 25 27 67 76 84 91 93
        # 93 92 89 69 68 66 26 17 9  2