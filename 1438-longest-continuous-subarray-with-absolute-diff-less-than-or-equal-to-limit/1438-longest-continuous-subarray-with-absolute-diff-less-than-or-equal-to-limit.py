class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx_h = []
        mn_h = []
        L = 0
        mx_len = 0
        for R in range(len(nums)):
            heapq.heappush(mx_h, (-nums[R], R))
            heapq.heappush(mn_h, (nums[R], R))
            while -mx_h[0][0] - mn_h[0][0] > limit:
                L = min(mx_h[0][1], mn_h[0][1]) + 1
                while mx_h[0][1] < L:
                    heapq.heappop(mx_h)
                while mn_h[0][1] < L:
                    heapq.heappop(mn_h)
            mx_len = max(mx_len, R - L + 1)
        return mx_len