class Twitter:

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

    def __init__(self):
        self.ff = defaultdict(set)
        self.tt = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tt[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, hh = [], []

        self.ff[userId].add(userId) # add yourself to the following list
        for f in self.ff[userId]:
            if f in self.tt:
                idx = len(self.tt[f]) - 1
                time, tweetId = self.tt[f][idx]
                heapq.heappush(hh, [time, tweetId, f, idx - 1])

        while hh and len(res) < 10:
            time, tweetId, f, idx = heapq.heappop(hh)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tt[f][idx]
                heapq.heappush(hh, [time, tweetId, f, idx - 1])
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.ff[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.ff[followerId]:
            self.ff[followerId].remove(followeeId)
            
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)