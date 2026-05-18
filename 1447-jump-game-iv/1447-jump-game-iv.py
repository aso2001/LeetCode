class Solution:
    def minJumps(self, arr: List[int]) -> int:

        same = {}
        visited = [False]*len(arr)

        for i in range(len(arr)):
            if arr[i] in same:
                same[arr[i]].append(i)
            else:
                same[arr[i]] = [i]

        q, nxt = [], []
        q.append(0)

        level = 0

        while q:
            for cur in q:
                if cur == len(arr) - 1:
                    return level
                for nei in same[arr[cur]]:
                    if not visited[nei]:
                        visited[cur] = True
                        nxt.append(nei)
                same[arr[cur]].clear()

                for nei in [cur - 1, cur + 1]:
                    if 0 <= nei < len(arr) and not visited[nei]:
                        visited[nei] = True
                        nxt.append(nei)
            q = nxt
            nxt = []
            level += 1
