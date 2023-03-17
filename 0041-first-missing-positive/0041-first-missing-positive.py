class Solution:
    def firstMissingPositive(self, n: List[int]) -> int:
        for i in range(len(n)):
            if n[i] < 0: n[i] = 0
        for i in range(len(n)):
            if 0 < abs(n[i]) <= len(n):     # valid number of array
                if n[abs(n[i]) - 1] > 0:
                    n[abs(n[i]) - 1] *= -1  # marking occupied positions in array
                elif n[abs(n[i]) - 1] == 0:
                    n[abs(n[i]) - 1] = -(len(n) + 1) # marking occupied positions in array

        for i in range(len(n)):
            if n[i] >= 0: return i + 1
        return len(n) + 1
    
    
    def firstMissingPositive2(self, nums: List[int]) -> int:
        n = nums
        cnt = 0
        imin = 10**31-1
        for i in range(len(n)):
            if n[i] <= 0:
                cnt += 1
                continue
            imin = min(imin, n[i])
        if imin > 1: return 1
        d = {}
        for i in range(len(n) - cnt + 1):
            d[i+1] = 0
        for i in range(len(n)):
            if n[i] > 0 and n[i] <= len(n) - cnt:
                d[n[i]] = 1
        for i in range(1, len(n) - cnt + 2):
            if d[i] == 0:
                return i