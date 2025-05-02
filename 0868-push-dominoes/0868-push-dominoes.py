class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        dom = list(dominoes)
        q = deque()
        for i in range(len(dom)):
            if dom[i] != '.':
                q.append(i)
        
        while q:
            i = q.popleft()
            if dom[i] == 'L' and i > 0 and dom[i - 1] == '.':
                dom[i - 1] = 'L'
                q.append(i - 1)
            elif dom[i] == 'R':
                if i + 1 < len(dom) and dom[i + 1] == '.':
                    if i + 2 < len(dom) and dom[i + 2] == 'L':
                        q.popleft()
                    else:
                        dom[i + 1] = 'R'
                        q.append(i + 1)
        return ''.join(dom)


    def pushDominoes2(self, dominoes: str) -> str:

        prev = list(dominoes)
        curr = prev.copy()
        
        while True:
            for i in range(len(dominoes)):
                if prev[i] == '.':
                    if i == 0:
                        if i < len(dominoes) - 1 and prev[i + 1] == 'L':
                            curr[i] = 'L'
                    elif i < len(dominoes) - 1:
                        if prev[i - 1] == 'L' and prev[i + 1] == 'R':
                            continue
                        elif prev[i - 1] != 'R' and prev[i + 1] == 'L':
                            curr[i] = 'L'
                        elif prev[i - 1] == 'R' and prev[i + 1] != 'L':
                            curr[i] = 'R'
                        elif prev[i - 1] == 'R' and prev[i + 1] == 'L':
                            curr[i] = '.'
                    elif i == len(dominoes) - 1:
                        if i > 0:
                            if prev[i - 1] == 'R':
                                curr[i] = 'R'

            if prev == curr:
                return ''.join(curr)
            else:
                prev = curr.copy()