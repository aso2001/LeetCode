class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Recursive solution using list sorting of candidates
        res2 = []

        def dfs(candidates, rem, res):
            if rem == 0:
                res2.append(res.copy())
                return

            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                if rem >= candidates[i]:
                    res.append(candidates[i])
                    dfs(candidates[i + 1:], rem - candidates[i], res)
                    res.pop()

        candidates.sort()
        dfs(candidates, target, [])
        return res2

