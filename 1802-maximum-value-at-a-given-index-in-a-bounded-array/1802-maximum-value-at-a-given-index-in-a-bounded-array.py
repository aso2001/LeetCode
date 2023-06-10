class Solution: 
    def maxValue3(self, n: int, index: int, maxSum: int) -> int:

        def ss(target):
            tt = target - 1
            ssum = 0
            for i in range(index, max(-1, index - target + 1), -1):
                ssum += tt
                tt -= 1
            tt = target - 2
            for i in range(index + 1, min(n, target - 1 + index)):
                ssum += tt
                tt -= 1
            return ssum + n

        L = 1
        R = maxSum
        while L < R:
            mid = (L + R)//2
            s0 = ss(mid)
            print(s0, L, R)
            if s0 < maxSum:
                L_prev = L
                L = mid + 1
            else:
                R = mid
            # else:
            #     return mid
        return L

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def ss(cnt, end):
            if cnt == 0:
                return 0
            start = max(end - cnt, 0)
            sum1 = end*(1 + end)//2
            sum2 = start*(1 + start)//2
            return sum1 - sum2

        maxSum -= n
        L, R = 0, maxSum
        while L <= R:
            mid = (L + R)//2
            lsum = ss(index + 1, mid)
            rsum = ss(n - index - 1, mid - 1)
            if lsum + rsum <= maxSum:
                L = mid + 1
            else:
                R = mid - 1
        return L
        
    def maxValue2(self, n: int, index: int, maxSum: int) -> int:
        # TLE solution
        if maxSum == n: return 1 
        ss = n + 1
        res = 2
        while True:
            if index - res < 0 and index + res >= n:
                ss += n
            elif index - res >= 0 and index + res >= n:
                ss += n - index - 1 + res
            elif index - res < 0 and index + res < n:
                ss += index + res
            elif index - res >= 0 and index + res < n:
                ss += 2*res - 1
            if ss > maxSum:
                return res
            res += 1