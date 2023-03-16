class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dd = {}
        for i in range(len(s)):
            dd[s[i]] = i
        res = []
        end = dd[s[0]]
        i = 0
        while end < len(s):
            while i <= end:
                if dd[s[i]] > end:
                    end = dd[s[i]]
                i += 1
            res.append(end + 1)
            if end < len(s) - 1:
                end += 1
            elif end == len(s) - 1:
                break
        for i in range(len(res) - 1, 0, -1):
            res[i] -= res[i - 1]
        return res