class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dd = {}
        for a, b in paths:
            if b not in dd:
                dd[b] = 2
            dd[a] = 1
        for a in dd.keys():
            if dd[a] == 2:
                return a