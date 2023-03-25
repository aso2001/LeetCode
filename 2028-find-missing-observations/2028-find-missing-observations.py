class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        res = []
        s1 = sum(rolls)
        n1 = len(rolls)
        ntot = n1 + n
        sm = mean * ntot - s1
        am = sm / (ntot - n1)
        ai = sm // (ntot - n1)
        if am > 6 or am < 1:
            return res
        x = ai*(ntot - n1) + ntot - n1 - sm
        res = [ai]*x
        res2 = [ai + 1]*(ntot - n1 - x)
        res.extend(res2) 
        return res