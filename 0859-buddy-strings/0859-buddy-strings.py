class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        dd = {}
        gg = {}
        if len(s) != len(goal): return False

        for ss in s:
            if ss in dd:
                dd[ss] += 1
            else:
                dd[ss] = 1
        for g in goal:
            if g in gg:
                gg[g] += 1
            else:
                gg[g] = 1                

        if s == goal:
            for d in dd:
                if dd[d] > 1:
                    return True
            return False

        if dd != gg:
            return False
            
        cnt = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                cnt += 1
        if cnt > 2:
            return False
        return True