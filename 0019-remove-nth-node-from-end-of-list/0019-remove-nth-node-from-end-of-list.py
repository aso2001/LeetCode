# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Two pointers solution (fast and slow)

        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            head = head.next
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if n == 1 and not head.next: return None
        length, cur, prev = 1, head, None
        while cur.next:
            prev, cur = cur, cur.next
            length += 1
        if n == length:
            head = head.next
            return head

        cnt, cur, prev = 1, head, None
        while cnt <= length - n:
            prev, cur = cur, cur.next
            cnt += 1
        prev.next = cur.next
        return head