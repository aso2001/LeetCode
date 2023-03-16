class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        import itertools
        dd = {}

        for w in ideas:
            if w[0] not in dd:
                dd[w[0]] = set()
            if w[1:] not in dd[w[0]]:
                dd[w[0]].add(w[1:])
                
        cmb = list(itertools.combinations(dd, 2))

        res = 0
        for c1, c2 in cmb:
            z1 = dd[c1].difference(dd[c2])
            z2 = dd[c2].difference(dd[c1]) 
            res += len(z1)*len(z2)

        return 2*res