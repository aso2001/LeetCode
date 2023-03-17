class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict:
                if len(dict[nums[i]]) == 1:
                    dd = dict[nums[i]]
                    dd.append(i)
                    dict[nums[i]] = dd
            else:
                dict[nums[i]] = [i]

        for i in range(len(nums)):
            if target - nums[i] == nums[i]:
                if len(dict[nums[i]]) == 2:
                    return dict[nums[i]]
                else:
                    continue
            else:
                if target - nums[i] in dict:
                    return [i,dict[target - nums[i]][0]]