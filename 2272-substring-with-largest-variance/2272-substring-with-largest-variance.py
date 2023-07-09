class Solution:  
    # Modified Kadane's Algo
    def largestVariance(self, s: str) -> int:    
        letters = set()
        for i in range(len(s)):
            letters.add(s[i])

        comb = [(l1, l2) for l1 in letters for l2 in letters if l1 != l2]
        #comb = list(itertools.combinations(letters, 2))
        mx = 0
        for c in comb:
            a, b = c[0], c[1]
            for r in range(2):
                freq1 = freq2 = 0
                for i in range(len(s)):
                    if s[i] != a and s[i] != b:
                        continue
                    if s[i] == a:
                        freq1 += 1
                    elif s[i] == b:
                        freq2 += 1
                    if freq1 < freq2:
                        freq1 = freq2 = 0
                    elif freq1 > 0 and freq2 > 0:
                        mx = max(mx, freq1 - freq2)
                s = s[::-1]
        return mx
    
    # TLE O(n**2)
    def largestVariance2(self, s: str) -> int:
        # a a b a b b b
        # -1 -1 1 -1 1 1 1
        # -1 -2 -1 -2 -1 0 1        
        # 1  2  3  2  3  2 1
        # 

        dd = {}
        letters = set()
        for i in range(len(s)):
            letters.add(s[i])
            if s[i] in dd:
                dd[s[i]].append(i)
            else:
                dd[s[i]] = [i]

        comb = list(itertools.combinations(letters, 2))
        mx = 0
        for c in comb:
            h = [0]*len(s)
            a, b = c[0], c[1]
            for i in dd[a]:
                h[i] = -1
            for i in dd[b]:
                h[i] = 1
            s0 = [0]*(len(s) + 1)
            s0[0] = 0
            for i in range(len(s)):
                s0[i + 1] = s0[i] + h[i]

            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    if s0[j] - s0[i] > 0 and s0[j] - s0[i] > mx:
                        for ii in dd[a]:
                            if ii >= i and ii <= j - 1:
                                mx = s0[j] - s0[i]
                                break
                    elif s0[j] - s0[i] < 0 and s0[i] - s0[j] > mx:
                        for ii in dd[b]:
                            if ii >= i and ii <= j - 1:
                                mx = s0[i] - s0[j]
                                break
        return mx