# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1, ll2 = [], []
        cur = l1
        while cur:
            ll1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            ll2.append(cur.val)
            cur = cur.next
        ll1 = ll1[::-1]
        ll2 = ll2[::-1]
        if len(ll2) > len(ll1):
            ll1, ll2 = ll2, ll1
        extra, i = 0, 0
        res = None
        while i < len(ll2):
            tmp = res
            res = ListNode((ll1[i] + ll2[i] + extra)%10)
            res.next = tmp
            extra = (ll1[i] + ll2[i] + extra)//10
            i += 1
        while i < len(ll1):
            tmp = res
            res = ListNode((ll1[i] + extra)%10)
            res.next = tmp
            extra = (ll1[i] + extra)//10
            i += 1
        if extra:
            tmp = res
            res = ListNode(extra)
            res.next = tmp
        return res