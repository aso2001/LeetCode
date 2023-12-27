class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = colors[0]
        tmp = [neededTime[0]]
        res = 0
        for i in range(1, len(colors)):
            if colors[i] == prev:
                tmp.append(neededTime[i])
            else:
                tmp.remove(max(tmp))
                res += sum(tmp)
                prev = colors[i]
                tmp = []
                tmp.append(neededTime[i])
        if colors[-1] == prev:
            tmp.remove(max(tmp))
            res += sum(tmp)
        return res