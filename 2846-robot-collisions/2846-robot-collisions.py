class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        idx = list(range(n))
        res = []
        stack = deque()
        idx.sort(key=lambda x: positions[x])
        for cur in idx:
            if directions[cur] == "R":
                stack.append(cur)
            else:
                while stack and healths[cur] > 0:
                    top_idx = stack.pop()
                    if healths[top_idx] > healths[cur]:
                        healths[top_idx] -= 1
                        healths[cur] = 0
                        stack.append(top_idx)
                    elif healths[top_idx] < healths[cur]:
                        healths[cur] -= 1
                        healths[top_idx] = 0
                    else:
                        healths[cur] = 0
                        healths[top_idx] = 0
        for index in range(n):
            if healths[index] > 0:
                res.append(healths[index])
        return res