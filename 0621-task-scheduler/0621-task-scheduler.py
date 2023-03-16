class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = {}
        for t in tasks:
            if t in cnt: cnt[t] += 1
            else: cnt[t] = 1

        hh = [-cnt[t] for t in cnt]
        heapq.heapify(hh)

        q = deque()
        
        time = 0
        while hh or q:
            time += 1
            if not hh:
                time = q[0][1]
            else:
                cur = heapq.heappop(hh)
                cur += 1
                if cur < 0:
                    q.append([cur, time + n])
            if q and q[0][1] == time:
                heapq.heappush(hh, q.popleft()[0])
        return time