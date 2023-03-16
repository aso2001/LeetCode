# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.start = head
        cnt = 0
        cur = head
        while cur:
            cur = cur.next
            cnt += 1
        self.length = cnt

    def getRandom(self) -> int:
        import random
        idx = random.randint(0, self.length - 1)
        cnt = 0
        cur = self.start
        while cnt != idx:
            cur = cur.next
            cnt += 1
        return cur.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()