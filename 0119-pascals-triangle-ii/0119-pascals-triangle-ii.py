class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex <= 1: 
            res = [1]*(rowIndex + 1)
            return res
        prev = [1,1]
        for i in range(2, rowIndex + 1):
            res = [1]*(i + 1)
            for j in range(1, i):
                res[j] = prev[j - 1] + prev[j]
            prev = res
        return res