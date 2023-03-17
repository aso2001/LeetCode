class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res, tmp = {"()"}, set()
        for _ in range(n - 1):
            for p in res:
                for i in range(len(p)):
                    tmp.add(p[:i] + "()" + p[i:])
                tmp.add("(" + p + ")")
            res, tmp = tmp, set()
        return res


    def generateParenthesis2(self, n: int) -> List[str]:
        # Recursive solution
        res = []

        def dfs(numO, numC, stack):
            if numO == numC == n:
                res.append("".join(stack))
                return

            if numO < n:
                dfs(numO + 1, numC, stack + ["("])
            
            if numO > numC:
                dfs(numO, numC + 1, stack + [")"])

        dfs(0, 0, [])
        return res