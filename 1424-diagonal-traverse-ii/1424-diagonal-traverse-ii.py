class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        i, j, dd, res = 0, 0, [], []
        for row in nums:
            j = 0
            for nn in row:
                tup = (i + j, i, nn)
                dd.append(tup)
                j += 1
            i += 1
        dd.sort(key = lambda x: (x[0], -x[1]))
        for d in dd:
            res.append(d[2])
        return res