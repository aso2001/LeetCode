class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if not n: return True
        if len(flowerbed) == 1:
            if not flowerbed[0]:
                return True
            return False

        cnt = i = 0
        while i < len(flowerbed) - 1:
            if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and (i == 0 or (i > 0 and flowerbed[i - 1] == 0)):
                cnt += 1
                if cnt == n:
                    return True
                flowerbed[i] = 1
            i += 2
        if flowerbed[-1] == 0 and len(flowerbed) > 1 and flowerbed[-2] == 0:
            if cnt + 1 == n:
                return True
        return False