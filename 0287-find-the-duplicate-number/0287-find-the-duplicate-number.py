class Solution:

    def findDuplicate(self, nums: List[int]) -> int:

        # Floyd's algo O(N) time, O(1) space
        slow, fast = 0, 0
        # Find cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find beginning of cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow2

            
    def findDuplicate2(self, nums: List[int]) -> int:

        slow1, slow2, fast = nums[0], 0, nums[nums[0]]

        # find cycle
        while slow1 != fast:
            slow1, fast = nums[slow1], nums[nums[fast]]

        # find start of cycle
        while slow1 != slow2:
            slow1, slow2 = nums[slow1], nums[slow2]

        return slow2
        # idx:       0 1 2 3 4
        # nums[idx]: 1 3 4 2 2    2 <-> 4 is cycle