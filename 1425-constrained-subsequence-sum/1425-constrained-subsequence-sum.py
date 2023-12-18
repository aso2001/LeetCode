class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        hh = [(-nums[0], 0)]
        res = nums[0]
        
        for i in range(1, len(nums)):
            while i - hh[0][1] > k:
                heapq.heappop(hh)

            cur = max(0, -hh[0][0]) + nums[i]
            res = max(res, cur)
            heapq.heappush(hh, (-cur, i))
        return res