class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}

        def dfs(alice, i):
            if i == len(stoneValue):
                return 0
            if (alice, i) in dp:
                return dp[(alice, i)]
            
            tot = 0
            if alice:
                res = -math.inf
                for j in range(1, min(len(stoneValue) - i + 1, 4)):
                    tot += stoneValue[i + j - 1]
                    res = max(res, tot + dfs(not alice, i + j))
                dp[(alice, i)] = res
            else:
                res = math.inf
                for j in range(1, min(len(stoneValue) - i + 1, 4)):
                    res = min(res, dfs(not alice, i + j))
                dp[(alice, i)] = res
            return res

        alice = dfs(True, 0)
        if 2*alice > sum(stoneValue):
            return 'Alice'
        elif 2*alice < sum(stoneValue):
            return 'Bob'
        elif 2*alice == sum(stoneValue):
            return 'Tie' 