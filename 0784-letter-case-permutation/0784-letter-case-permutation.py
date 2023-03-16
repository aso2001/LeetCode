class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = [s]
        for i in range(len(s)):
            if s[i].isalpha():
                nres = []
                if s[i].islower():
                    for r in res:
                        tmp = list(r)
                        tmp[i] = tmp[i].upper()
                        new = "".join(tmp)
                        nres.append(new)
                else:
                    for r in res:
                        tmp = list(r)
                        tmp[i] = tmp[i].lower()
                        new = "".join(tmp)
                        nres.append(new)
                res.extend(nres)
        return res