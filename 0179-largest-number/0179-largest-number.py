class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        def cmp(a, b):
            return -1 if a + b > b + a else 1

        nums.sort(key = cmp_to_key(cmp))
        if nums[0] == '0': return '0'
        return ''.join(nums)


    def largestNumber2(self, nums: List[int]) -> str:

        def cmp(a, b):
            if not a: return 1
            elif not b: return -1
            db = math.floor(math.log(b) / math.log(10)) + 1
            da = math.floor(math.log(a) / math.log(10)) + 1
            return 1 if a*10**db + b < b*10**da + a else -1

        nums.sort(key = cmp_to_key(cmp))
        for i in range(len(nums)): 
            nums[i] = str(nums[i])
        if nums[0] == '0': return '0'
        return ''.join(nums)