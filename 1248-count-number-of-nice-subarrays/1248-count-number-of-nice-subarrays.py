class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= 2
        
        pfx_cnt = [0] * (len(nums) + 1)
        pfx_cnt[0] = 1
        s = 0
        res = 0
        
        for num in nums:
            s += num
            if s >= k:
                res += pfx_cnt[s - k]
            pfx_cnt[s] += 1
        return res