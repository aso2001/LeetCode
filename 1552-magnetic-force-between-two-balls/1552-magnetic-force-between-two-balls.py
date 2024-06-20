class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def check(x):
            cnt = 0
            prev = position[0]
            for i in range(1, len(position)):
                if position[i] - prev >= x:
                    cnt += 1
                    prev = position[i]
            return True if cnt >= (m - 1) else False

        position.sort()
        print(position)
        L, R = 1, int((position[-1] - position[0])/(m-1))
        while L <= R:
            mid = (L + R) // 2
            if check(mid):
                res = mid
                L = mid + 1
            else:
                R = mid - 1
        return res