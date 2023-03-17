# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next: return None
        slow, fast = head.next, head.next.next

        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next

        if slow != fast:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return None

        slow = head.next
        fast = head.next.next

        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next

        if slow != fast:
            return None

        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow