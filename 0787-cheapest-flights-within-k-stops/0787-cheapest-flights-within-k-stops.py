class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        d = [math.inf]*n
        r = defaultdict(list)
        for i, j, w in flights: r[i].append([j, w])

        queue = [(0,src,0)]
        while queue:
            w, i, st = queue.pop(0)
            if d[i] <= w or (st > k and i != dst):
                continue
            d[i] = w
            for j, wj in r[i]:
                queue.append((w + wj, j, st + 1))

        return -1 if d[dst] == math.inf else d[dst]