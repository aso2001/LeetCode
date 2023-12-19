class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r = len(img)
        c = len(img[0])
        moves = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        res = [[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                cnt, tot = 1, img[i][j]
                for m in moves:
                    if i + m[0] < 0 or i + m[0] == r or j + m[1] < 0 or j + m[1] == c:
                        continue
                    cnt += 1
                    tot += img[i + m[0]][j + m[1]]
                res[i][j] = math.floor(tot/cnt)
        return res