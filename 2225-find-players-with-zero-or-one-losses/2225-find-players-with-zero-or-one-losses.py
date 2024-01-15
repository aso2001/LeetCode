class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dl = {}
        a = [set(),[]]
        for m in matches:
            if m[1] in dl:
                dl[m[1]] = 0
            else:
                dl[m[1]] = 1
        for m in matches:
            if m[0] not in dl:
                a[0].add(m[0])
        for d in dl:
            if dl[d] == 1:
                a[1].append(d)
        a[0] = list(a[0])
        a[0].sort()
        a[1].sort()
        return a