# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        dummy.next = head
        prev = dummy
        while head:
            if head.next:
                # Swap pointers
                tmp = head.next
                head.next = head.next.next
                prev.next = tmp
                tmp.next = head
                # Move 
                prev = head
                head = head.next
            else:
                break
        return dummy.next

    
    def swapPairs2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        cur = head
        while cur:
            if cur.next:
                tmp = cur.next
                cur.next = cur.next.next
                prev.next = tmp
                tmp.next = cur

                prev = cur
                cur = cur.next
            else:
                break
        return dummy.next