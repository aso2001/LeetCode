class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Greedy O(n)
        if sum(gas) < sum(cost): return -1
        gsum = 0
        res = 0
        for i in range(len(gas)):
            gsum += gas[i] - cost[i]
            if gsum < 0:
                gsum = 0
                res = i + 1
        return res
    

    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        while i < len(gas) and gas[i] < cost[i]:
            i += 1
        if i == len(gas): return -1
        st = i
        while st < len(gas):
            gsum = 0
            flag = 0
            for i in range(st, len(gas)):
                gsum += gas[i] - cost[i]
                if gsum < 0:
                    flag = 1
                    st = i + 1
                    break
            if flag == 1:
                continue
            for i in range(0, st):
                gsum += gas[i] - cost[i]
                if gsum < 0:
                    flag = 1
                    st += 1
                    break
            if flag == 1:
                continue
            return st
        if flag == 1:
            return -1