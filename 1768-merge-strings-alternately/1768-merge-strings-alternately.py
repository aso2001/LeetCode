class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])
        while i < max(len(word1), len(word2)) - 1:
            i += 1
            if len(word1) >= len(word2):
                res.append(word1[i])
            else:
                res.append(word2[i])
                       
        return ''.join(res)