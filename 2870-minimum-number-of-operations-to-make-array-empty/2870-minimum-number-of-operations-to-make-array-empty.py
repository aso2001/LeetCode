class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dd = {}
        for n in nums:
            if n in dd:
                dd[n] += 1
            else:
                dd[n] = 1
        res = 0
        for d in dd:
            if dd[d] == 1:
                return -1
            if not dd[d] % 3:
                res += dd[d] // 3
            elif dd[d] % 3 == 1:
                res += dd[d] // 3 - 1
                res += 2
            elif dd[d] % 3 == 2:
                res += dd[d] // 3 + 1
            elif not dd[d] % 2:
                res += dd[d] // 2
            else:
                return -1
        return res