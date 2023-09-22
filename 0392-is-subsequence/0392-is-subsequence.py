class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not t:
            if not s:
                return True
            else:
                return False
        j = 0
        cnt = 0
        for i in range(len(s)):
            while j < len(t) - 1:
                if t[j] == s[i]:
                    cnt += 1
                    j += 1
                    break
                j += 1
            if j == len(t) - 1:
                if cnt == len(s) - 1:
                    if s[len(s)-1] == t[j]:
                        return True
                    else:
                        return False
                if cnt == len(s):
                    return True
                else:
                    return False
        return True