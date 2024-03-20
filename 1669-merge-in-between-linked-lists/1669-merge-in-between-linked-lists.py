# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        cnt = 0
        cur = list1
        while cnt != a - 1:
            cur = cur.next
            cnt += 1
        nxt = cur.next
        while cnt != b - 1:
            nxt = nxt.next
            cnt += 1
        cur.next = list2
        while cur.next:
            cur = cur.next
        cur.next = nxt.next
        return list1