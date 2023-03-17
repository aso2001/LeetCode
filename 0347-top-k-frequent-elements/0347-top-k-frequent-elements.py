class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = {}
        ans = []
        res = [[] for _ in range(len(nums))]
        for nn in nums:
            if nn not in dd:
                dd[nn] = 1
            else:
                dd[nn] += 1
        for d in dd:
            res[dd[d] - 1].append(d)
        while True:
            if res[-1] != []:
                for n in res[-1]:
                    ans.append(n)
                    if len(ans) == k:
                        return ans
            res.pop()