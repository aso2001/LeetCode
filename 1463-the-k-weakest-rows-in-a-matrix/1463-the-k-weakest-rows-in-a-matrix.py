class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i in range(len(mat)):
            cnt = 0
            for j in range(len(mat[0])):
                if mat[i][j]:
                    cnt += 1
            pair = [cnt, i]
            res.append(pair)
        res.sort(key=lambda x: x[0], reverse = False)
        res = res[0:k]
        ans = []
        for c in res:
            ans.append(c[1])
        return ans 