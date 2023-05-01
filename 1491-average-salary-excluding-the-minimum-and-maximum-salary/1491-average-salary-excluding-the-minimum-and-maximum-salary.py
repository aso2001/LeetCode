class Solution:
    def average(self, salary: List[int]) -> float:
        mn, mx, res = math.inf, -math.inf, 0
        imn, imx = -1, -1
        for i in range(len(salary)):
            if salary[i] < mn:
                mn = salary[i]
                imn = i
            if salary[i] > mx:
                mx = salary[i]
                imx = i
            res += salary[i]
        if imn == imx:
            res -= mn
            res /= len(salary) - 1
        else:
            res -= mn + mx
            res /= len(salary) - 2
        return res