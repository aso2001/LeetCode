# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        L = head
        mid = self.findMid(L)
        R = mid.next
        mid.next = None     # Find middle and cut the linked list after middle node

        L = self.sortList(L)
        R = self.sortList(R)
        return self.merge(L, R)

    def merge(self, L, R):
        tail = dummy = ListNode()
        while L and R:
            if L.val < R.val:
                tail.next = L
                L = L.next
            else:
                tail.next = R
                R = R.next
            tail = tail.next
        if L:
            tail.next = L
        if R:
            tail.next = R
        return dummy.next
    
    def findMid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:  # return first middle element if odd number of nodes
            slow = slow.next
            fast = fast.next.next
        return slow