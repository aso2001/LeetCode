class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, seq = [], []

        def backtrack(i, j):
            if j == k:
                res.append(seq.copy())
            for ii in range(i, n + 1):
                seq.append(ii)
                backtrack(ii + 1, j + 1)
                seq.pop()

        backtrack(1, 0)
        return res