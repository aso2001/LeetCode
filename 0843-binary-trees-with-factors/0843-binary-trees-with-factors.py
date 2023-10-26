class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        arr.sort()
        dd = {}
        for a in arr:
            dd[a] = 1
        for a in arr:
            for factor in arr:
                if factor == a:
                    break
                if a % factor == 0 and a // factor in dd:
                    dd[a] += dd[factor] * dd[a//factor]
        return sum(dd.values()) % mod