class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        for c in s1:
            if c in d: d[c] += 1
            else: d[c] = 1
                
        i, flag = 0, 0
        while i < len(s2):
            if s2[i] not in d:
                i += 1
                continue
            else:
                d1 = d.copy()
                if d1[s2[i]] == 1: del d1[s2[i]]
                else: d1[s2[i]] -= 1
                if not d1: return True
                j = i + 1
                while j < len(s2):
                    if s2[j] in d1:
                        if d1[s2[j]] == 1: del d1[s2[j]]
                        else: d1[s2[j]] -= 1
                        if not d1: return True
                    else:
                        if s2[j] == s2[i]:
                            i += 1
                        else:
                            flag = 1
                            del d1
                            break
                    j += 1
                if flag == 1:
                    i += 1
                    flag = 0
                else:
                    i = j
        return False