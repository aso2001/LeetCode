class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def check(s):
            return True if s == s[::-1] else False

        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                ss = s[i:j + 1]
                if check(ss):
                    part.append(ss)
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res