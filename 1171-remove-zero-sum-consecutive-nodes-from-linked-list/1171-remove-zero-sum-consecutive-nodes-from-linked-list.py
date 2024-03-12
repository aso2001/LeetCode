# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        start = front

        while start:
            pfx = 0
            end = start.next

            while end:
                pfx += end.val
                if not pfx:
                    start.next = end.next
                end = end.next
            start = start.next
        return front.next