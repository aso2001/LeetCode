class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = deque(senate)
        while len(senate) > 2:
            if senate.popleft() == 'R':
                try:
                    senate.remove('D')
                except ValueError:
                    return 'Radiant'
                senate.append('R')
            else:
                try:
                    senate.remove('R')
                except ValueError:
                    return 'Dire'
                senate.append('D')
        return 'Radiant' if senate.popleft() == 'R' else 'Dire'