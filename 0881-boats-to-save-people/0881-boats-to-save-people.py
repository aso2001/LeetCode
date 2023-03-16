class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse = True)
        res, L, R = 0, 0, len(people) - 1
        while L <= R:
            if people[L] == limit:
                res += 1
                L += 1
            elif people[L] + people[R] <= limit:
                res += 1
                L += 1
                R -= 1
            else:
                res += 1
                L += 1
        return res