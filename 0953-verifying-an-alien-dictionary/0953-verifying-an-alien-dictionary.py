class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d, dn, nwords = {}, {}, []
        a = 'abcdefghijklmnoprqstuvwxyz'
        for i in range(26):
            d[order[i]] = i
            dn[i] = a[i]

        for w in words:
            s = [""]*len(w)
            for i in range(len(w)):
                s[i] = dn[d[w[i]]]
            nw = "".join(s)
            nwords.append(nw)
        words = nwords.copy()
        nwords.sort()
        return words == nwords