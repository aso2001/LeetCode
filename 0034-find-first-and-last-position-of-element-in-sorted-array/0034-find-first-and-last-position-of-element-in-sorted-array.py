class Solution:
    def searchRange(self, n: List[int], t: int) -> List[int]:
        LL = self.binarySearch(n, t, 1)
        RR = self.binarySearch(n, t, 0)
        return [LL,RR]

    def binarySearch(self, n, t, left_bias):
        L, R, match = 0, len(n) - 1, -1
        while L <= R:
            mid = (L + R)//2
            if t < n[mid]: R = mid - 1
            elif t > n[mid]: L = mid + 1
            else: 
                match = mid
                if left_bias:
                    R = mid - 1
                else:
                    L = mid + 1
        return match

    
    def searchRange2(self, n: List[int], t: int) -> List[int]:
        L, R, match = 0, len(n) - 1, -1
        while L <= R:
            mid = (L + R)//2
            if t < n[mid]: R = mid - 1
            elif t > n[mid]: L = mid + 1
            else: 
                match = mid
                break
        if match == -1:  return [-1, -1]

        i, j, LL, RR = match, match, match, match
        
        while i >= 0 and n[i] == t:
            LL = i
            i -= 1
        while j <= len(n) - 1 and n[j] == t:
            RR = j
            j += 1
        return [LL, RR]