class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mx = [[0]*n for _ in range(n)]
        # Range caching
        for r1, c1, r2, c2 in queries:
            mx[r1][c1] += 1
            if r2 + 1 < n:
                mx[r2+1][c1] -= 1
            if c2 + 1 < n:
                mx[r1][c2+1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                mx[r2+1][c2+1] += 1
                
        for r in range(1, n):
            for c in range(n):
                mx[r][c] += mx[r-1][c]
        for r in range(n):
            for c in range(1,n):
                mx[r][c] += mx[r][c-1]
        return mx

        # [0 0 0 0 0 0]
        # [0 1 2 2 0 0]
        # [0 1 1 0 -2 0]
        # [0 1 2 2 0 0]