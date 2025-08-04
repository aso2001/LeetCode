class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        mx, L, dd = 0, 0, {}

        for R in range(len(fruits)):
            if fruits[R] in dd:
                dd[fruits[R]] += 1
            else:
                dd[fruits[R]] = 1
                while len(dd) == 3:
                    dd[fruits[L]] -= 1
                    if dd[fruits[L]] == 0:
                        del dd[fruits[L]]
                    L += 1
            mx = max(mx, sum(dd.values()))
        return mx