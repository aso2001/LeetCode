class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        q, cnt, rooms = [], [0]*n, [0]*n

        for j in range(len(meetings)):
            done = False
            for i in range(len(rooms)):
                if not done and meetings[j][0] >= rooms[i]:
                    done = True
                    cnt[i] += 1
                    rooms[i] = meetings[j][1]
                    if q:
                        nxt, room = heapq.heappop(q)
                        if room != i:
                            heapq.heappush(q, (nxt, room))
                    heapq.heappush(q, (meetings[j][1], i))
            if not done:
                nxt, room = heapq.heappop(q)
                cnt[room] += 1
                if nxt <= meetings[j][0]:
                    heapq.heappush(q, (meetings[j][1], room))
                    rooms[room] = meetings[j][1]
                else:
                    heapq.heappush(q, (meetings[j][1] - meetings[j][0] + nxt, room))
                    rooms[room] = meetings[j][1] - meetings[j][0] + nxt
        res, mx = -1, -1
        for i in range(n):
            if cnt[i] > mx:
                mx = cnt[i]
                res = i
        return res