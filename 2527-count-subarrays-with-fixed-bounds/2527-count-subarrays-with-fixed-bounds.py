class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        minSeen, maxSeen = 0, 0
        start, minBeg, maxBeg = 0, 0, 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                minSeen = 0
                maxSeen = 0
                start = i + 1
            if nums[i] == minK:
                minSeen = 1
                minBeg = i
            if nums[i] == maxK:
                maxSeen = 1
                maxBeg = i
            if minSeen and maxSeen:
                res += (min(minBeg, maxBeg) - start + 1)
        return res
    #2 3 1 2 5 4 3 1 2 6 5 4 3 1