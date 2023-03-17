class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        q = deque()
        L = R = 0

        while R < len(nums):
            while q and nums[q[-1]] <= nums[R]:  # pop smaller values from queue
                q.pop()
            q.append(R)

            if L > q[0]:    # remove left value from window
                q.popleft()

            if R + 1 >= k:
                res.append(nums[q[0]])
                L += 1
            R += 1
        return res

    
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:

        res = []
        q = deque()
        for i in range(k):
            while q and q[-1][0] < nums[i]:
                q.pop()
            q.append((nums[i], i))
        
        res.append(q[0][0])

        for i in range(k, len(nums)):
            if q[0][1] <= i - k:
                q.popleft()
            while q and q[-1][0] <= nums[i]:
                q.pop()
            if not q:
                res.append(nums[i])
            else:
                res.append(q[0][0])
            q.append((nums[i], i))
        return res