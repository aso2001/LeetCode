class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1 : return False
        d = max(abs(fx - sx), abs(fy - sy))
        return True if t >= d else False