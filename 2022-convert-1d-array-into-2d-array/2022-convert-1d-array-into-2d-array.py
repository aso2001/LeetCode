class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        res = []
        ln = len(original)
        if ln % n or ln % m or ln / m != n:
            return []
        for i in range(m):
            res.append(original[i*n:(i+1)*n])
        return res