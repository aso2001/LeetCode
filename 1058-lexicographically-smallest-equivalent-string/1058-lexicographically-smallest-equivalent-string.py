class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        parent = list(range(26))
        for a, b in zip(s1, s2):
            x, y = ord(a) - 97, ord(b) - 97
            rx, ry = find(x), find(y)
            if rx != ry:
                if rx < ry: parent[ry] = rx
                else:       parent[rx] = ry

        res = []
        for c in baseStr:
            r = find(ord(c) - 97)
            res.append(chr(r + 97))

        return ''.join(res)