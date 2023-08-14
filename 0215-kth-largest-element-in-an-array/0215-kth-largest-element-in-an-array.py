class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        hh = []

        for n in nums:
            heapq.heappush(hh, -n)
        for i in range(k):
            res = heapq.heappop(hh)
        return -res
    
    
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # MinHeap Solution O(n + k*log(n))
        import heapq
        for i in range(len(nums)):
            nums[i] = - nums[i]
        heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)
        return -res

    
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        # Solution using Quick Select Algorithm O(n) time on average
        k = len(nums) - k

        def quickSelect(l, r):
            p = l
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k: return quickSelect(l, p - 1)
            elif p < k: return quickSelect(p + 1, r)
            else: return nums[p]

        return quickSelect(0, len(nums) - 1)