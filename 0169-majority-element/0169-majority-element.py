class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Moore's Majority Voting Algorithm
        cnt = 0
        res = nums[0]
        for n in nums:
            if n == res:
                cnt += 1
            else:
                if cnt > 0:
                    cnt -= 1
                else:
                    res = n
        
        # Second pass to check majority candidate
        cnt = 0
        for n in nums:
            if n == res: cnt += 1
        return res if cnt > len(nums)//2 else -1