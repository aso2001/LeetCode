class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cc = {}
        res = 0
        for c in chars:
            if c in cc:
                cc[c] += 1
            else:
                cc[c] = 1
        for w in words:
            ww = {}
            for c in w:
                if c in ww:
                    ww[c] += 1
                else:
                    ww[c] = 1
            flag = 0
            for c in w:
                if c in cc and cc[c] >= ww[c]:
                    continue
                else:
                    flag = 1
                    break
            if flag == 0:
                res += len(w)
        return res