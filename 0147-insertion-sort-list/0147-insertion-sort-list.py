# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tail = dummy = ListNode()
        dummy.next = head       # append node before head for simple code traverse list and insert before head
        while tail.next:        # iterate from head to tail
            cur = tail.next     # end of sorted part of the list
            pos = dummy
            while pos.next != cur and cur.val >= pos.next.val:  # scan sorted part of list to find position for cur to place
                pos = pos.next
            if pos.next == cur: # if no position exist leave cur at current position and increment tail of sorted part
                tail = tail.next
            else:               # insert cur into position after pos and before pos.next (pos is previous element pos -> cur -> pos.next) and update end of sorted part
                tail.next = cur.next
                cur.next = pos.next
                pos.next = cur
        return dummy.next


    def insertionSortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head.next
        prevc = head
        cnt = 0
        flag = 0
        while cur:
            pos = head
            prevp = None
            while pos != cur:
                cnt += 1
                if cur.val < pos.val:
                    tmp = cur.next
                    if pos != head:
                        prevp.next = cur
                    prevc.next = cur.next
                    if pos == head:
                        head = cur
                    cur.next = pos
                    cur = tmp
                    flag = -1
                    break
                prevp = pos
                pos = pos.next
            if flag == -1:
                flag = 0
            else:
                prevc = cur
                cur = cur.next
        return head