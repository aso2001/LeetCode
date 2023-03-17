class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Sliding window solution
        d = {}
        
        L, smax = -1, 0
        for R in range(len(s)):
            if s[R] in d:
                if d[s[R]] > L:
                    L = d[s[R]]
            d[s[R]] = R
            smax = max(smax, R - L)
        return smax

    
    def lengthOfLongestSubstring2(self, s: str) -> int:
        if s == "": return 0
        d = {}

        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            if len(d) == 26 or len(d) == len(s):
                break
        ld = len(d)
        d.clear()

        i, jmax = 0, 0
        while i < len(s):
            if s[i] not in d:
                d[s[i]] = i
                i += 1
                if i == len(s):
                    return max(jmax,len(d))
            else:
                if jmax < len(d):
                    jmax = len(d)
                if jmax == ld:
                    return jmax
                tmp = d[s[i]]
                d.clear()
                i = tmp + 1

        return jmax         