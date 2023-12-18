class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            nn = nums[l[i]:r[i]+1]
            nn.sort()
            if r[i] - l[i] <= 1:
                if r[i] - l[i] < 1:
                    res.append(False)
                else:
                    res.append(True)
                continue
            dif = nn[1] - nn[0]
            for j in range(2,len(nn)):
                if nn[j] - nn[j - 1] != dif:
                    res.append(False)
                    break
            if len(res) == i:
                res.append(True)
        return res