# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        c1, c2, cur = None, None, head
        while cur:
            if cur.val < x:
                if not c1:
                    c1 = ListNode(cur.val)
                    c1.next = None
                    head1 = c1
                else:
                    tmp1 = ListNode(cur.val)
                    tmp1.next = None
                    c1.next = tmp1
                    c1 = tmp1
            elif cur.val >= x:
                if not c2:
                    c2 = ListNode(cur.val)
                    c2.next = None
                    head2 = c2
                else:
                    tmp2 = ListNode(cur.val)
                    tmp2.next = None
                    c2.next = tmp2
                    c2 = tmp2
            cur = cur.next
        if c1 and c2:
            c1.next = head2
            return head1
        elif c1 and not c2:
            return head1
        elif not c1 and c2:
            return head2