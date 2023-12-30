class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dd = {}
        for w in words:
            for c in w:
                if c in dd:
                    dd[c] += 1
                else:
                    dd[c] = 1
        for c in dd:
            if dd[c] % len(words):
                return False
        return True