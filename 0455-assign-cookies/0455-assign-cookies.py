class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)

        res, i = 0, 0
        for gg in g:
            if i == len(s):
                break
            if gg <= s[i]:
                res += 1
                i += 1
        return res