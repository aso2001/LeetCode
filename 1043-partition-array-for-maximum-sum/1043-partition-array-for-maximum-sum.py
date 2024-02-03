class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dd = {}

        def dfs(i):
            if i >= len(arr):
                return 0
            if i in dd:
                return dd[i]
            cur_max = 0
            res = 0
            for j in range(i, min(i + k, len(arr))):
                cur_max = max(cur_max, arr[j])
                window = j - i + 1
                res = max(res, dfs(j + 1) + cur_max*window)
            dd[i] = res
            return res

        return dfs(0)