class Solution:
    def get_num_of_bouquets(self, bloomDay, mid, k):
        res = 0
        cnt = 0
        for day in bloomDay:
            if day <= mid:
                cnt += 1
            else:
                cnt = 0
            if cnt == k:
                res += 1
                cnt = 0
        return res

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        start = 0
        end = max(bloomDay)
        minDays = -1
        while start <= end:
            mid = (start + end) // 2
            if self.get_num_of_bouquets(bloomDay, mid, k) >= m:
                minDays = mid
                end = mid - 1
            else:
                start = mid + 1
        return minDays