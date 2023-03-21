class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # O(n) time O(1) space solution 
        res = cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            else:
                cnt = 0
            res += cnt
        return res


    def zeroFilledSubarray2(self, nums: List[int]) -> int:
        
        res = [0]*len(nums)
        flag = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if flag == 0:
                    res[i] = 1
                    flag = 1
                else:
                    res[i] = res[i - 1] + 1
            else:
                flag = 0
        return sum(res)