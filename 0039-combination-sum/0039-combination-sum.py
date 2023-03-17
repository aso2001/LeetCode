class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Recursive backtracking without duplicates
        res2 = []

        def dfs(i, rem, res):
            if rem == 0:
                res2.append(res.copy())
                return
            if i == len(candidates):
                return
            if rem >= candidates[i]:
                res.append(candidates[i])
                dfs(i, rem - candidates[i], res)
                res.pop()
            dfs(i + 1, rem, res)
            
        dfs(0, target, [])
        return res2
    

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Backtracking solution with duplicate paths    
        minC = min(candidates)

        def dfs(rem, res, res2):
            if rem == 0:
                tmp = res.copy()
                tmp.sort()
                res2.add(tuple(tmp))
                return
            elif rem < minC:
                return
            for c in candidates:
                if rem >= c:
                    res.append(c)
                    dfs(rem - c, res, res2)
                    res.pop()

        res, res2 = [], set()
        dfs(target, res, res2)
        return res2