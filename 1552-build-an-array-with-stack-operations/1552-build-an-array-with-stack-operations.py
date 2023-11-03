class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i = 1
        for t in target:
            while i < t:
                res.append('Push')
                res.append('Pop')
                if i == n: return res
                i += 1
            res.append('Push')
            if i == n: return res
            i += 1
        return res