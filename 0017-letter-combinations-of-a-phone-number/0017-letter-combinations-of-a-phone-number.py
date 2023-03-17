class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0: return []
        d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        res = [_ for _ in d[digits[0]]]
        if len(digits) == 1: return res
        if len(digits) >= 2:
            for i in range(1, len(digits)):
                id1, id2, tmp = res, digits[i], []
                for di1 in id1:
                    for di2 in d[id2]:
                        tmp.append(di1 + di2)
                res = tmp
        return res
    
    
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "": return []
        ld = len(digits)
        dd = [0]*ld
        idigits = int(digits)
        d = [[] for _ in range(8)]
        d[2-2] = ["a","b","c"]
        d[3-2] = ["d","e","f"]
        d[4-2] = ["g","h","i"]
        d[5-2] = ["j","k","l"]
        d[6-2] = ["m","n","o"]
        d[7-2] = ["p","q","r","s"]
        d[8-2] = ["t","u","v"]
        d[9-2] = ["w","x","y","z"]

        i = ld - 1
        while idigits > 0:
            dd[i] = idigits%10
            i -= 1
            idigits //= 10

        res = d[dd[0] - 2]
        if ld == 1: return res
        if ld >= 2:
            for i in range(1, ld):
                id1 = res
                id2 = dd[i]
                res2 = []
                for di1 in id1:
                    for di2 in d[id2 - 2]:
                        res2.append(di1 + di2)
                res = res2
        return res