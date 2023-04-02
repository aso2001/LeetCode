class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []

        def helper(x):
            L, R = 0, len(potions) - 1
            while L < R:
                mid = (L + R) // 2
                if success <= x*potions[mid]:
                    R = mid
                elif success > x*potions[mid]:
                    L = mid + 1
            if success > x*potions[L] and L + 1 < len(potions):
                return L + 1
            elif success <= x*potions[L]:
                return L
            else: 
                return -1

        for s in spells:
            idx = helper(s)
            if idx == -1:
                res.append(0)
            else:
                res.append(len(potions) - idx)
        return res