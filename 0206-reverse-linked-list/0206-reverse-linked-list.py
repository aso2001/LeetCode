# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #Iterative solution
    
        cur = head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
    
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Recursive solution
    
        return self.reverseHelper(head, None)
            
    def reverseHelper(self, head, node):
        if not head:
            return node
        tmp = head.next
        head.next = node
        return self.reverseHelper(tmp, head)

