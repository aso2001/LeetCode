class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        lt = len(target)
        lw = len(words[0])

        dd = [[0]*len(words[0]) for _ in range(26)]
        for j in range(len(words[0])):
            for i in range(len(words)):
                dd[ord(words[i][j]) - ord('a')][j] += 1
        
        dp = defaultdict(int)

        def dfs(i, j):
            if j == lt:
                return 1
            if i == lw:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            cur = target[j]
            dp[(i, j)] = dfs(i + 1, j)
            if dd[ord(cur) - ord('a')][i]:
                dp[(i, j)] += dd[ord(cur) - ord('a')][i] * dfs(i + 1, j + 1)
            return dp[(i, j)] % (10**9 + 7)
        
        return dfs(0, 0)

