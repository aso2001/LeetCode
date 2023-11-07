class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = [0] * len(dist)
        for i in range(len(dist)):
            times[i] = ceil(dist[i] / speed[i])
        times.sort()
        print(times)
        res = 0
        i = 0
        while i < len(times) and times[i] > i: 
            res += 1
            i += 1
        return res