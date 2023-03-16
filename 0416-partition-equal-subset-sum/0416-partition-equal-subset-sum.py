class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        @cache
        def dfs(i, target):
            if i == len(nums):
                return False
            if target == 0:
                return True
            elif nums[i] > target:
                return False
            return dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
        
        ss = sum(nums)
        if ss%2: return False
        ss /= 2
        return dfs(0, ss)

    
    def canPartition2(self, nums: List[int]) -> bool:
        # TLE Solution (Too slow)
        ss = sum(nums)
        if ss%2: return False
        ss /= 2
        memo = {}

        def backtrack(s, num):
            for i in range(len(num)):                
                if s + num[i] > ss:
                    continue
                elif s + num[i] == ss:
                    return True
                elif (ss - num[i], i) in memo:
                    return memo[(ss - num[i], i)]
                else:
                    nn = num.copy()
                    nn.remove(num[i])
                    s += num[i]
                    if not backtrack(s, nn):
                        s -= num[i]
                        nn.append(num[i])
            return False
        return backtrack(0, nums)