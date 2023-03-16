class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1 or n == 2: return 1
        else:
            arr = [0]*(n + 2)
            arr[1] = arr[2] = 1
            for i in range(3, n + 1):
                arr[i] = arr[i - 3] + arr[i - 2] + arr[i - 1]
            return arr[n]