class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1: return False
        dd = {}
        for d in deck:
            if d in dd: dd[d] += 1
            else: dd[d] = 1
        
        mind = min(dd.values())
        for i in range(2, mind + 1):
            m = True
            for d in dd:
                if dd[d]%i:
                    m = False
            if m == True:
                return True
        return False