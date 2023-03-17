class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                if -(nums[L] + nums[R]) < nums[i]:
                    R -= 1
                elif -(nums[L] + nums[R]) > nums[i]:
                    L += 1
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L-1] and L < R:
                        L += 1
        return res

       
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d: d[nums[i]] += 1
            else: d[nums[i]] = 1
        
        res = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums)):
                if -(nums[i] + nums[j]) in d:
                    dd = -(nums[i] + nums[j])
                    if (dd == nums[i] or dd == nums[j]):
                        if d[dd] == 1 or (dd == 0 and d[dd] == 2):
                            continue
                    cand = [nums[i], nums[j], dd]
                    cand.sort()
                    res.append(cand)
        res = list(set(map(tuple, res)))
        return res