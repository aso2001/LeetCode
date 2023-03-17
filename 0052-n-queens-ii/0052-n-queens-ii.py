class Solution:
    def totalNQueens(self, n: int) -> int:
        col, pdi, ndi = set(), set(), set()
        res = 0

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return
            for c in range(n):
                if c in col or (r + c) in pdi or (r - c) in ndi:
                    continue

                col.add(c)
                pdi.add(r + c)
                ndi.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                pdi.remove(r + c)
                ndi.remove(r - c)

        backtrack(0)
        return res