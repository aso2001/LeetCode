class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        res = []
        m = len(rolls)
        nsum = mean * (m + n) - sum(rolls)
        an = nsum / n
        ai = nsum // n
        if an > 6 or an < 1:
            return res
        x = ai*n + n - nsum
        res = [ai]*x
        res2 = [ai + 1]*(n - x)
        res.extend(res2) 
        return res