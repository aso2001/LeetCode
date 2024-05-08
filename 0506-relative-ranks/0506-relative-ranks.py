class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = ['0']*len(score)
        for i in range(len(score)):
            rank[i] = str(i + 1)
        rank[0] = 'Gold Medal'
        if len(score) >=2 :
            rank[1] = 'Silver Medal'
        if len(score) >= 3:
            rank[2] = 'Bronze Medal'
        arr = [tuple]*len(score)
        for  i in range(len(score)):
            arr[i] = (score[i],i)
        arr.sort(reverse = True)
        res = [0]*len(score)
        for i in range(len(score)):
            res[arr[i][1]] = rank[i]
        return res