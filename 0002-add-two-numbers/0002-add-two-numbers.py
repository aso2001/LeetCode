# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1, n2, s = 0, 0, 0

        cnt = 0
        node = l1
        while node:
            n1 += node.val*(10**cnt)
            cnt += 1
            node = node.next

        cnt = 0
        node = l2
        while node:
            n2 += node.val*(10**cnt)
            cnt += 1
            node = node.next

        s = n1 + n2
        l3 = ListNode(s%10)
        prev = l3
        s //= 10
        while s > 0:
            node = ListNode(s%10)
            prev.next = node
            prev = node
            s //= 10
        return l3