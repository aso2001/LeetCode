class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        mx = int(''.join(['1']*n), 2)
        for i in range(mx + 1):
            bi = bin(i)
            print(bi)
            bb = bi[2:]
            if len(bb) < n:
                xtra = ''.join(['0']*(n - len(bb)))
                bb = xtra + bb
            if bb in nums:
                continue
            else:
                return bb
        return -1