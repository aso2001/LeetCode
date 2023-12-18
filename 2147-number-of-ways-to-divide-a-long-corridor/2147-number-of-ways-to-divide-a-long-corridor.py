class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10 ** 9 + 7
        cache = [[-1]*3 for _ in range(len(corridor))]

        def count(idx, seats):
            if idx == len(corridor):
                return 1 if seats == 2 else 0
            if cache[idx][seats] != -1:
                return cache[idx][seats]
            if seats == 2:
                if corridor[idx] == "S":
                    res = count(idx + 1, 1)
                else:
                    res = (count(idx + 1, 0) + count(idx + 1, 2)) % mod
            else:
                if corridor[idx] == "S":
                    res = count(idx + 1, seats + 1)
                else:
                    res = count(idx + 1, seats)
            
            cache[idx][seats] = res
            return cache[idx][seats]

        return count(0, 0)    