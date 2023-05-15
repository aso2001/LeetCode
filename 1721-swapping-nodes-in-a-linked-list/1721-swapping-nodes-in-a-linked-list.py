# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        cnt = 0
        prev = dummy
        cur = head
        while cnt < k - 1:
            prev = cur
            cur = cur.next
            cnt += 1
        prev1 = prev
        cur1 = cur

        n = cnt
        while cur:
            cur = cur.next
            n += 1
                     
        cnt = 0
        prev = None
        cur = dummy
        while cnt < n - k + 1:
            prev = cur
            cur = cur.next
            cnt += 1
        prev2 = prev
        cur2 = cur

        if cur1.next != cur2 and cur2.next != cur1:
            tmp1 = cur1.next
            tmp2 = cur2.next
            prev1.next = cur2
            cur2.next = tmp1
            prev2.next = cur1
            cur1.next = tmp2
        elif cur1.next == cur2:
            tmp = cur2.next
            prev1.next = cur2
            cur2.next = cur1
            cur1.next = tmp
        else:
            tmp = cur1.next
            prev2.next = cur1
            cur1.next = cur2
            cur2.next = tmp
            
        return dummy.next  