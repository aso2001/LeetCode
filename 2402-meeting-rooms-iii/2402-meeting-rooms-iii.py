class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [0]*n
        cnt = [0]*n
        done = [0]*len(meetings)
        q = []

        for j in range(len(meetings)):
            for i in range(len(rooms)):
                if not done[j] and meetings[j][0] >= rooms[i]:
                    cnt[i] += 1
                    rooms[i] = meetings[j][1]
                    done[j] = 1
                    if q:
                        tt,rr = heapq.heappop(q)
                        if rr != i:
                            heapq.heappush(q, (tt, rr))
                    heapq.heappush(q, (meetings[j][1], i))
            if not done[j]:
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