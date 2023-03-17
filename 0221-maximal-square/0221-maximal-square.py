class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        mx = matrix
        mx = [[int(x) for x in row] for row in mx]
        m = len(mx)
        n = len(mx[0])
        if not mx:
            return 0
    
        cnt = 0
        for i in range(m):
            for j in range(n):
                if i and j and mx[i][j]:
                    mx[i][j] = 1 + min(mx[i-1][j], mx[i][j-1], mx[i-1][j-1])
                cnt = max(cnt,mx[i][j])
        
        return cnt**2
    

    def maximalSquare2(self, matrix: List[List[str]]) -> int:

        mxx = matrix
        mx = [list(map(int,i)) for i in mxx]
        m = len(mx)
        n = len(mx[0])
        if not any(any(_) for _ in mx):
            return 0
        if m == 1 or n == 1:
            return max(map(max, mx))
        
        s = [[0]*(n-1) for _ in range(m-1)]

        cnt = 0

        while True:
            for i in range(m-1):
                for j in range(n-1):
                    if mx[i][j] == 0:
                        continue
                    s[i][j] = 1 if mx[i][j] + mx[i+1][j] + mx[i][j+1] + mx[i+1][j+1] == 4 else 0
            cnt += 1
            if not any(any(_) for _ in s):  # check if matrix is Zero
                return cnt*cnt
            m -= 1
            n -= 1
            mx = [[0]*n for _ in range(m)]
            mx = s
            s = [[0]*(n-1) for _ in range(m-1)]
