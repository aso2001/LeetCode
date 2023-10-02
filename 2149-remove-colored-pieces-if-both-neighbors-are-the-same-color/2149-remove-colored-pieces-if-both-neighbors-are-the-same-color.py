class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cca, ccb = 0, 0
        ca, cb = 0, 0
        for c in colors:
            if c == 'A':
                if cb:
                    if cb >= 3:
                        ccb += cb - 2
                    cb = 0
                ca += 1
            elif c == 'B':
                if ca:
                    if ca >= 3:
                        cca += ca - 2
                    ca = 0
                cb += 1
        if ca >= 3:
            cca += ca - 2 
        if cb >= 3:
            ccb += cb - 2   
        return True if cca > ccb else False