class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())

    def longestStrChain2(self, w: List[str]) -> int:
        w = sorted(w, key = lambda x: (len(x), x))
        n = len(w)

        dd = {}
        for i in range(n):
            dd[w[i]] = 1

        d = [list() for i in range(len(w[0]), len(w[n-1])+1)]
        for i in range(n):
            d[len(w[i])-len(w[0])].append(w[i])

        if n == 1:
            return 1

        def check(a, b):
            if len(b) - len(a) != 1:
                return False
            for i in range(len(a)):
                if a[i] != b[i] and a[i] != b[i+1]:
                    return False
            return True

        prev = d[0]
        for i in range(1, len(d)):
            curr = d[i]
            for j in range(len(curr)):
                for k in range(len(prev)):
                    if check(prev[k], curr[j]) and dd[curr[j]] <= dd[prev[k]]:
                        dd[curr[j]] = dd[prev[k]] + 1
            prev = curr

        return max(dd.values())