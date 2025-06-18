class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0,len(nums),3):
            triple = nums[i:i+3]
            if triple[2] - triple[0] <= k:
                res.append(triple)
            else:
                return []
        return res