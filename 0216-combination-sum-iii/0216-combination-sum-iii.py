class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res, comb = [], []

        def backtrack(i):
            if len(comb) == k and sum(comb) == n:
                res.append(comb.copy())
                return

            for ii in range(i, 10):
                if sum(comb) + ii > n:
                    return
                comb.append(ii)
                backtrack(ii + 1)
                comb.pop()
        
        backtrack(1)
        return res