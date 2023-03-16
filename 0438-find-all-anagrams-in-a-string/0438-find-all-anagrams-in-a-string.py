class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dp = {c:p.count(c) for c in p}
        ds = {c:s[:len(p)].count(c) for c in s[:len(p)]}

        res, i = [], 0

        while i <= len(s) - len(p):
            if ds == dp:
                res.append(i)
            if i == len(s) - len(p):
                break

            if ds[s[i]] > 1: 
                ds[s[i]] -= 1
            else: 
                del ds[s[i]]

            if s[i + len(p)] in ds: 
                ds[s[i + len(p)]] += 1
            else: 
                ds[s[i + len(p)]] = 1
            i += 1
        return res
    

    def findAnagrams2(self, s: str, p: str) -> List[int]:

        dd = {c:p.count(c) for c in p}

        res, i, flag = [], 0, 0

        while i <= len(s) - len(p):
            while i <= len(s) - len(p) and s[i] not in dd:
                i += 1
            dd1 = dd.copy()
            for j in range(i, min(i + len(p),len(s))):
                if s[j] in dd1 and dd1[s[j]] > 0:
                    dd1[s[j]] -= 1
                else:
                    flag = 1
                    break
            if flag == 0 and sum(dd1.values()) == 0:
                res.append(i)
                i += 1
                while i <= len(s) - len(p) and s[i - 1] == s[i + len(p) - 1]:
                    res.append(i)
                    i += 1
            flag = 0
            i += 1
        return res