class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = [[1]]
        lev = [1]

        for i in range(numRows - 1):
            lev.append(0)
            prev = lev
            lev = [1]
            for j in range(i + 1):
                lev.append(prev[j] + prev[j + 1])
            res.append(lev[::-1])
        return res

    # 1,4,6,4,1
    # 1,5,10,10,5,1
    # 1,6,15,20,15,6,1