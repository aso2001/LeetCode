class Solution:
    def clearStars(self, s: str) -> str:
        q = []
        for i in range(len(s)):
            if s[i] == '*':
                heapq.heappop(q)
            else:
                pair = (s[i],-i)
                heapq.heappush(q,pair)
        res = ['']*len(s)
        while q:
            c, i = heapq.heappop(q)
            res[-i] = c
        return ''.join(res)
            