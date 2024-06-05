class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dd = defaultdict(int)
        for c in words[0]:
            dd[c] += 1
        for i in range(1, len(words)):
            dd2 = defaultdict(int)
            for c in words[i]:
                if c in dd and dd[c] > 0:
                    dd2[c] += 1
                    dd[c] -= 1
            dd = dd2
        res = []
        for c in dd:
            res.extend([c]*dd[c])
        return res