class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        if len(nums)%k: return False
        
        dd = {}
        for n in nums:
            if n in dd: dd[n] += 1
            else: dd[n] = 1

        minH = list(dd.keys())
        heapq.heapify(minH)
        while minH:
            start = minH[0]
            for i in range(start, start + k):
                if i not in dd:
                    return False
                dd[i] -= 1
                if dd[i] == 0: # pop from heap all used elements dd[i] = 0
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True