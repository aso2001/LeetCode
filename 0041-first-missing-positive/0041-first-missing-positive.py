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