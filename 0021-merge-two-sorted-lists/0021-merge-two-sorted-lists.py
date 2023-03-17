# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next

    
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        cur1, cur2, head = list1, list2, list1
        if cur1 and cur2:
            if cur1.val > cur2.val:
                head, cur2 = cur2, cur2.next
            else:
                head, cur1 = cur1, cur1.next
        else:
            if cur1: head = cur1
            elif cur2: head = cur2
            return head

        cur = head
        while True:
            if cur1 and cur2:
                if cur1.val > cur2.val:
                    cur.next, cur2 = cur2, cur2.next
                else:
                    cur.next, cur1 = cur1, cur1.next
                cur = cur.next   
            else:
                if cur1: cur.next = cur1
                elif cur2: cur.next = cur2
                return head