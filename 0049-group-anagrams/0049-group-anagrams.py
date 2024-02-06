class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        dd = defaultdict(list)
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp in dd:
                dd[tmp].append(s)
            else:
                dd[tmp] = [s]
        return dd.values()

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:    
        res = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()