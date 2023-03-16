class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = 0, 0, 0
        for t0, t1, t2 in triplets:
            if t0 <= target[0] and t1 <= target[1] and t2 <= target[2]:
                a = max(a, t0)
                b = max(b, t1)
                c = max(c, t2)
        return [a, b, c] == target

    def mergeTriplets2(self, triplets: List[List[int]], target: List[int]) -> bool:
        c0, c1, c2 = [], [], []
        for t in triplets:
            if t[0] == target[0]:
                c0.append(t)
            if t[1] == target[1]:
                c1.append(t)
            if t[2] == target[2]:
                c2.append(t)
        if len(c0) == len(c1) == len(c2) == 1 and c0 == c1 == c2:
            return True
        if not c0 or not c1 or not c2:
            return False

        flag = 0
        for c in c0:
            if c[1] <= target[1] and c[2] <= target[2]:
                flag = 1
        if flag == 0:
            return False
        flag = 0
        for c in c1:
            if c[0] <= target[0] and c[2] <= target[2]:
                flag = 1
        if flag == 0:
            return False
        flag = 0
        for c in c2:
            if c[0] <= target[0] and c[1] <= target[1]:
                flag = 1
        if flag == 0:
            return False
        return True