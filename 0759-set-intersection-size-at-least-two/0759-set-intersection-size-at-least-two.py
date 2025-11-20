class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda e: (e[1], -e[0]))
        prev = [intervals[0][1], intervals[0][1]-1]
        ans = 2
        for (s, e) in intervals:
            elements_added = 0
            for index in range(2):
                if not (s <= prev[index] <= e):
                    prev[index] = e-elements_added
                    elements_added += 1
            ans += elements_added
        return ans