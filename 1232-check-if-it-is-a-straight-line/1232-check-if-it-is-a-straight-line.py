class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2: return True
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        if x1 != x0: k = (y1 - y0)/(x1 - x0)
        else:
            for x,y in coordinates[2:]:
                if x != x0:
                    return False
            return True
        for x,y in coordinates[2:]:
            if x != x0:
                if k != (y - y0)/(x - x0):
                    return False
            else:
                return False
        return True