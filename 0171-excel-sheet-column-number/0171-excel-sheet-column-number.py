class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for c in columnTitle:
            res = 26*res + ord(c) - ord("A") + 1
        return res

    
    def titleToNumber2(self, columnTitle: str) -> int:
        res, cnt = 0, 0
        for c in reversed(columnTitle):
            res += 26**cnt*(ord(c) - ord("A") + 1)
            cnt += 1
        return res