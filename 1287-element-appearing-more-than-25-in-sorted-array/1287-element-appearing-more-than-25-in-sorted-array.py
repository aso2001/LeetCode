class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = int(len(arr)/4) + 1
        cnt = 0
        if n == 1: return arr[0]
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                cnt += 1
            else:
                cnt = 0
            if cnt == n - 1:
                return arr[i]