class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        psum, cnt, dd = 0, 0, {}
        for i in range(len(nums)):
            psum += nums[i]
            if psum % k not in dd:
                dd[psum % k] = 1
            else:
                dd[psum % k] += 1
        for d in dd:
            if dd[d] > 1:
                cnt += math.comb(dd[d], 2)
        if 0 in dd:
            cnt += dd[0]
        return cnt