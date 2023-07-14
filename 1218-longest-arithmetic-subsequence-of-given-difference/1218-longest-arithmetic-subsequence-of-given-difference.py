class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        seen = collections.Counter()
        for a in arr:
            seen[a] = seen[a - difference] + 1
        return max(seen.values())

    def longestSubsequence2(self, arr: List[int], difference: int) -> int:
        dif = difference
        visited = [False]*len(arr)
        res = 1
        for i in range(len(arr)):
            cnt = 1
            if visited[i]:
                continue
            arr1 = arr[i]
            visited[i] = True
            j = i
            while j + 1 < len(arr) and arr1 + dif in arr[j+1:]:
                k = arr.index(arr1 + dif, j+1)
                visited[k] = True
                j = k
                cnt += 1
                arr1 += dif
            res = max(cnt, res)
        return res