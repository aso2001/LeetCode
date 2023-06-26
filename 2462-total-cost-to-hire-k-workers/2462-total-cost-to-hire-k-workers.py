class Solution:
    def totalCost(self, costs: List[int], k: int, n: int) -> int:
        i = 0
        j = len(costs) - 1
        h1 = []
        h2 = []

        res = 0
        while k > 0:
            while len(h1) < n and i <= j:
                heapq.heappush(h1, costs[i])
                i += 1
            while len(h2) < n and i <= j:
                heapq.heappush(h2, costs[j])
                j -= 1

            t1 = h1[0] if h1 else float('inf')
            t2 = h2[0] if h2 else float('inf')

            if t1 <= t2:
                res += t1
                heapq.heappop(h1)
            else:
                res += t2
                heapq.heappop(h2)
            k -= 1
        return res