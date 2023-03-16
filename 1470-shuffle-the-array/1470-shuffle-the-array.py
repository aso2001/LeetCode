class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        if n == 1: return nums
        for i in range(1, n, 1):
            nums[i] = nums[i] * 10000 + i
        
        j = 1
        for i in range(n, 2*n - 1):
            nums[j], nums[i] = nums[i], nums[j]
            j += 2

        for i in range(2, 2*n - 1, 2):
            tmp = nums[i]
            while tmp > 1000:
                val = int(tmp/10000)
                idx = tmp % 10000
                nxt = nums[idx*2]
                tmp = nxt
                nums[idx*2] = val          
        return nums

        # 1 2 3 4 5 6 7 8 9 10 11 12 13 14
        # 1 8 3 4 5 6 7 2 9 10 11 12 13 14
        # 1 8 3 9 5 6 7 2 4 10 11 12 13 14
        # 1 8 3 9 5 10 7 2 4 6 11 12 13 14
        # 1 8 3 9 5 10 7 11 4 6 2 12 13 14
        # 1 8 3 9 5 10 7 11 4 12 2 6 13 14
        # 1 8 3 9 5 19 7 11 4 12 2 13 6 14
        #     3   5    7    4    2    6

        # 10,000*nums[i] + i