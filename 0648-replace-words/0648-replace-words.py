class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dd = []
        for d in dictionary:
            dd.append((len(d), d))
        dd.sort()
        res = []
        flag = -1
        ss = sentence.split(" ")
        for s in ss:
            for d in dd:
                if s.find(d[1]) == 0:
                    flag = 1
                    res.append(d[1])
                    break
            if flag == -1:
                res.append(s)
            flag = -1
        return ' '.join(res)