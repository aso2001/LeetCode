class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        rem = [target - p for p in position]
        time = [r/s for r,s in zip(rem,speed)]
        #print('\n','sped', speed, '\n', 'dist', rem, '\n','time', time)

        nn = list(zip(rem,time))
        nn = sorted(nn, key = lambda x: x[0])
        cnt = 1
        i, j = 0, 1
        while i < len(nn) and j < len(nn):
            while j < len(nn) and nn[i][1] >= nn[j][1]:
                j += 1
                continue
            if j == len(nn):
                break
            cnt += 1
            i = j
            j += 1
        return cnt