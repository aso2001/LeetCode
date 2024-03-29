class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        res, L, R = 0, 0, len(tokens) - 1
        while L <= R:
            if tokens[L] <= power:
                res += 1
                power -= tokens[L]
                L += 1
            elif L < R and res >= 1:
                res -= 1
                power += tokens[R]
                R -= 1
            else:
                return res
        return res