class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target: return True
            if nums[L] == nums[mid]: 
                L += 1
                continue
            if nums[L] <= nums[mid]:
                if nums[L] <= target <= nums[mid]: R = mid - 1
                else: L = mid + 1
            else:
                if nums[mid] <= target <= nums[R]: L = mid + 1
                else: R = mid - 1
        return False  