# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Solution using no extra memory space
        # Find middle and cut list into 2 halfs
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        p2 = mid.next
        mid.next = None

        # Reverse 2nd half
        prev = None
        while p2:
            tmp = p2.next
            p2.next = prev
            prev = p2
            p2 = tmp
        p2 = prev  # p2 is head of 2nd half
        p1 = head  # p1 is head of 1st half
        # Merge 2 halfs
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2
            
            
    def reorderList2(self, head: Optional[ListNode]) -> None:
        # Solution using stack
        stack = []
        slow = head
        fast = head.next
        # Find middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        # Save in stack second half
        while slow.next:
            slow = slow.next
            stack.append(slow)
        mid.next = None # cut the list at the middle
        node = head
        while stack:
            tmp = node.next
            cur = stack.pop()
            node.next = cur
            cur.next = tmp
            node = tmp