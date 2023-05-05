class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = cnt = 0
        for i in range(k):
            if s[i] in ['a','e','i','o','u']:
                cnt += 1
        res = cnt
        for i in range(k, len(s)):
            if s[i] in ['a','e','i','o','u']:
                if s[i - k] not in ['a','e','i','o','u']:
                    cnt += 1
            else:
                if s[i - k] in ['a','e','i','o','u']:
                    cnt -= 1
            res = max(res, cnt)
        return res