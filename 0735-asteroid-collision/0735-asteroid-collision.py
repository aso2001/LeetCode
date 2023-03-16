class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        a = asteroids

        res, i, flag = [], 0, 0
        while i < len(a):
            if not res or a[i] > 0:
                res.append(a[i])
            else:
                while res and res[-1] > 0:
                    if res[-1] > abs(a[i]):
                        flag = 1
                        break
                    elif res[-1] == abs(a[i]):
                        res.pop()
                        flag = 1
                        break
                    else:
                        res.pop()
                if flag == 0:
                    res.append(a[i])
                else:
                    flag = 0
            i += 1
        return res 