class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ic = isConnected
        n = len(ic)
        visited = [False]*n

        d = [list() for i in range(n)]
        for i in range(n):
            for j in  range(n):
                if ic[i][j] and i != j:
                    d[i].append(j)

        cnt = 0
        stack = []
        stack.append(0)

        while True:
            if stack:
                curr = stack.pop()
                visited[curr] = True
                if d[curr]:
                    for v in d[curr]:
                        if not visited[v]:
                            stack.append(v)
            else:
                cnt += 1
                for i in range(n):
                    if not visited[i]:
                        stack.append(i)
                        break
                if not stack:
                    return cnt