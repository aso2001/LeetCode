class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cur = [poured]
        for row in range(query_row):
            nxt = [0]*(row + 2)
            for g in range(len(cur)):
                extra = (cur[g] - 1) / 2
                if extra > 0:
                    nxt[g] += extra
                    nxt[g + 1] += extra
            cur = nxt

        return min(1, cur[query_glass])