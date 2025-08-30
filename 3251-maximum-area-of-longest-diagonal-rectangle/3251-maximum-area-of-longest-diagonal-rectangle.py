class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dim = dimensions
        dmx = 0
        amx = 0
        for d in dim:
            dig = sqrt(d[0]*d[0] + d[1]*d[1])
            a = d[0]*d[1]
            if dig > dmx:
                amx = a
                dmx = dig
            elif dig == dmx and a > amx:
                amx = a
        return amx