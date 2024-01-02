class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        cnt, mx = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                cnt += 1
            else:
                mx = max(mx, cnt)
                cnt = 1
        mx = max(mx, cnt)   
        res = [[] for _ in range(mx)]
        res[0] = [nums[0]]
        j = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                j += 1
                res[j].append(nums[i])
            else:
                j = 0
                res[j].append(nums[i])
        return res