class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j, cnt = 0, len(nums) - 1, 0
        while i <= j:
            if nums[i] == val:
                while nums[j] == val and j > i:
                    j -= 1
                    cnt += 1
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                cnt += 1
            i += 1
        return  len(nums) - cnt