# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        if left == 1:
            cur = dummy
            cnt = 0
        else:
            cnt = 1
            cur = head
        while cur and cur.next and cnt != left - 1:
            cur = cur.next
            cnt += 1
        pleft1 = cur
        pleft = cur.next

        cur, cnt = head, 1
        while cur and cnt != right:
            cur = cur.next
            cnt += 1
        pright = cur
        pright1 = cur.next

        cur = pleft
        prev = pright.next
        while cur != pright:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        cur.next = prev
        pleft1.next = cur
        pleft.next = pright1

        return dummy.next